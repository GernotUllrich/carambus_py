import subprocess
from urllib.parse import urljoin
import requests
from django.db import models, connection
from django.core.management import call_command
from django.conf import settings
from django.apps import apps


class Version(models.Model):
    event = models.CharField(max_length=255, null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)
    object = models.TextField(null=True, blank=True)
    object_changes = models.TextField(null=True, blank=True)
    whodunnit = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["item_type", "item_id"]),
        ]

    @classmethod
    def list_sequence(cls):
        sql = """
SELECT 'SELECT NEXTVAL(' ||
       quote_literal(quote_ident(pg_class_table.schemaname) || '.' || quote_ident(sequences.relname)) || ') FROM ' ||
       quote_ident(pg_class_table.schemaname)|| '.'||quote_ident(tables.relname)|| ';' as query
FROM pg_class AS sequences,
     pg_depend AS dependencies,
     pg_class AS tables,
     pg_attribute AS attributes,
     pg_tables AS pg_class_table
WHERE sequences.relkind = 'S'
    AND sequences.oid = dependencies.objid
    AND dependencies.refobjid = tables.oid
    AND dependencies.refobjid = attributes.attrelid
    AND dependencies.refobjsubid = attributes.attnum
    AND tables.relname = pg_class_table.tablename
ORDER BY sequences.relname;
        """
        with connection.cursor() as cursor:
            cursor.execute(sql)
            queries = cursor.fetchall()
            for query in queries:
                cursor.execute(query[0])

    @classmethod
    def update_carambus(cls):
        url = urljoin(settings.CARAMBUS_API_URL, "/versions/current_revision")
        response = requests.get(url)
        response.raise_for_status()

        revision = response.json().get("current_revision")
        with open(f"{settings.BASE_DIR}/REVISION", "r") as file:
            current_revision = file.read().strip()

        if current_revision != revision:
            command = f"REVISION={revision} bash -x {settings.BASE_DIR}/bin/deploy.sh 2>&1"
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            print(result.stdout)
        else:
            print(f"Carambus version is up-to-date ({revision})")

    @classmethod
    def max_ids(cls):
        call_command("makemigrations", "--dry-run", "--verbosity=3", stdout=open("/dev/null", "w"))
        models_with_ids = []
        output = []

        for model in apps.get_models():
            try:
                max_id = model.objects.latest("id").id
            except model.DoesNotExist:
                max_id = None

            if max_id and max_id > settings.MIN_ID:
                models_with_ids.append(model.__name__)

            output.append(f"{model.__name__}: {max_id}")

        return output, models_with_ids

    @classmethod
    def sequence_reset(cls):
        if settings.LOCAL_SERVER:
            sql = """
            SELECT 'SELECT SETVAL(' ||
                   quote_literal(quote_ident(pg_class_table.schemaname) || '.' || quote_ident(sequences.relname)) ||
                   ', GREATEST(COALESCE(MAX(' ||quote_ident(attributes.attname)|| '), 1), CAST(50000000 AS BIGINT)) ) FROM ' ||
                   quote_ident(pg_class_table.schemaname)|| '.'||quote_ident(tables.relname)|| ';' as query
            FROM pg_class AS sequences,
                 pg_depend AS dependencies,
                 pg_class AS tables,
                 pg_attribute AS attributes,
                 pg_tables AS pg_class_table
            WHERE sequences.relkind = 'S'
                AND sequences.oid = dependencies.objid
                AND dependencies.refobjid = tables.oid
                AND dependencies.refobjid = attributes.attrelid
                AND dependencies.refobjsubid = attributes.attnum
                AND tables.relname = pg_class_table.tablename
            ORDER BY sequences.relname;
            """
            with connection.cursor() as cursor:
                cursor.execute(sql)
                queries = cursor.fetchall()
                for query in queries:
                    cursor.execute(query[0])
        else:
            with connection.cursor() as cursor:
                for table in connection.introspection.table_names():
                    model = apps.get_model(table.capitalize())
                    if model:
                        objects_to_remove = model.objects.filter(id__gt=50000000)
                        objects_to_remove.delete()

                        max_id = model.objects.aggregate(models.Max("id"))["id__max"]
                        if max_id:
                            cursor.execute(f"SELECT setval('{table}_id_seq', {max_id + 1})")

    # Other methods like last_version, update_from_carambus_api, etc., can be implemented similarly.
