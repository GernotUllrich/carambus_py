from django.core.management.base import BaseCommand
from django.db import connections
from django.apps import apps


class Command(BaseCommand):
    help = 'Check the existence of all necessary tables in the database'

    def handle(self, *args, **kwargs):
        # Get the default database connection
        connection = connections['default']
        cursor = connection.cursor()

        # Get all model tables
        models = apps.get_models()

        missing_tables = []
        for model in models:
            table_name = model._meta.db_table
            try:
                cursor.execute(f"SELECT 1 FROM {table_name} LIMIT 1;")
            except Exception as e:
                missing_tables.append(table_name)

        if not missing_tables:
            self.stdout.write(self.style.SUCCESS("All necessary tables are present in the database."))
        else:
            self.stdout.write(self.style.ERROR("The following tables are missing:"))
            for table in missing_tables:
                self.stdout.write(self.style.ERROR(table))

        # Close the cursor
        cursor.close()
