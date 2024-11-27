# list_managed_models.py
import os
import django
from django.core.management.base import BaseCommand
from django.db import connections
from django.apps import apps

class Command(BaseCommand):
    help = ('list all models_xxx managed by Django')

    def handle(self, *args, **kwargs):
        all_models = apps.get_models()
        managed_models = []
        unmanaged_models = []

        for model in all_models:
            if model._meta.managed:
                managed_models.append(model)
            else:
                unmanaged_models.append(model)

        # Print managed models_xxx
        print("Managed Models:")
        for model in managed_models:
            print(f"- {model._meta.app_label}.{model.__name__}")

        # Print unmanaged models_xxx
        print("\nUnmanaged Models:")
        for model in unmanaged_models:
            print(f"- {model._meta.app_label}.{model.__name__}")

