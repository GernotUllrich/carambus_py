from django.core.management.base import BaseCommand
from carambus_py.models import Version

class Command(BaseCommand):
    help = "Retrieve updates from the API server"

    def handle(self, *args, **options):
        self.stdout.write("Starting to retrieve updates from API server...")

        for i in range(1, 11):  # Loop from 1 to 10
            Version.update_from_carambus_api()
            self.stdout.write(f"Iteration {i}: update_from_carambus_api called.")

        self.stdout.write("Finished retrieving updates.")
