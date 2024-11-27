import subprocess
from urllib.parse import urljoin
import requests
from django.db import models, connection
from django.core.management import call_command
from django.conf import settings
from django.apps import apps
from carambus_py.models import Season, Setting



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
        # TODO update_carambus for python hast to be implemented
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
    @classmethod
    def update_from_carambus_api(cls, opts=None):
        if opts is None:
            opts = {}
        tournament_id = opts.get("update_tournament_from_ba")
        region_id = (
                opts.get("reload_tournaments")
                or opts.get("reload_leagues")
                or opts.get("reload_leagues_with_details")
                or opts.get("update_region_from_ba")
        )
        league_id = opts.get("update_league_from_ba")
        club_id = opts.get("update_club_from_ba")
        force = opts.get("force")
        player_details = opts.get("player_details")
        league_details = opts.get("league_details")

        last_version_id = int(Setting.key_get_value("last_version_id", 0))
        base_url = f"{settings.CARAMBUS_API_URL}/versions/get_updates"
        params = {
            "last_version_id": last_version_id,
            "update_tournament_from_ba": tournament_id,
            "reload_tournaments": opts.get("reload_tournaments") and region_id,
            "reload_leagues": opts.get("reload_leagues") and region_id,
            "reload_leagues_with_details": opts.get("reload_leagues_with_details") and region_id,
            "update_region_from_ba": opts.get("update_region_from_ba") and region_id,
            "update_club_from_ba": club_id,
            "update_league_from_ba": league_id,
            "force": force,
            "player_details": player_details,
            "league_details": league_details,
            "season_id": Season.current_season().id,
        }

        # Remove keys with None values
        params = {k: v for k, v in params.items() if v is not None}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            vers = response.json()
        except requests.HTTPError as e:
            print(f"HTTPError: {e} while accessing {base_url}")
            return str(e)

        while vers:
            h = vers.pop(0)
            if not h:
                break

            last_version_id = h.get("id", 0)
            event = h.get("event")
            item_type = h.get("item_type")
            item_id = h.get("item_id")
            object_changes = h.get("object_changes")
            object_data = h.get("object")

            if event == "create":
                cls.handle_create_event(item_type, item_id, object_changes)

    # Other methods like last_version, update_from_carambus_api, etc., can be implemented similarly.
