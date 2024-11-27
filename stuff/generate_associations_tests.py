import os
import re
from django.db import models
from django.apps import apps
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carambus_py.settings")

# Initialize Django
django.setup()

# Path to save the test file
TEST_FILE_PATH = "tests_associations.py"


def get_association_tests():
    """Generates test cases for associations in all rails_models."""
    test_cases = []
    test_cases.append("from django.test import TestCase\n")
    test_cases.append("from django.db import IntegrityError\n")
    test_cases.append("\n# Import all rails_models")

    # Dynamically import all rails_models
    for app_config in apps.get_app_configs():
        if app_config.models_module:  # Skip apps without rails_models
            app_name = app_config.name
            for model in app_config.get_models():
                model_name = model.__name__
                test_cases.append(f"from {app_name}.rails_models import {model_name}")

    test_cases.append("\n\nclass AssociationTests(TestCase):\n")

    for app_config in apps.get_app_configs():
        if app_config.models_module:
            for model in app_config.get_models():
                model_name = model.__name__
                test_cases.append(f"from {app_name}.rails_models import {model_name}")

                print(f"Processing model: {model_name}")  # Debug output
                fields = model._meta.get_fields()

                for field in fields:
                    print(f"  Field: {field.name} ({type(field).__name__})")  # Debug field types

                # Generate tests for associations
                for field in fields:
                    if isinstance(field, models.ForeignKey):
                        related_model = field.related_model.__name__
                        test_cases.append(
                            f"    def test_{model_name.lower()}_{field.name}_foreign_key(self):\n"
                            f"        \"\"\"Test {model_name}.{field.name} ForeignKey to {related_model}\"\"\"\n"
                            f"        try:\n"
                            f"            obj = {model_name}.objects.create({field.name}={related_model}.objects.create())\n"
                            f"            self.assertIsNotNone(obj.{field.name})\n"
                            f"        except IntegrityError:\n"
                            f"            self.fail('{model_name}.{field.name} ForeignKey creation failed')\n"
                            f"\n"
                        )
                    elif isinstance(field, models.OneToOneField):
                        related_model = field.related_model.__name__
                        test_cases.append(
                            f"    def test_{model_name.lower()}_{field.name}_one_to_one_field(self):\n"
                            f"        \"\"\"Test {model_name}.{field.name} OneToOneField to {related_model}\"\"\"\n"
                            f"        try:\n"
                            f"            obj = {model_name}.objects.create({field.name}={related_model}.objects.create())\n"
                            f"            self.assertIsNotNone(obj.{field.name})\n"
                            f"        except IntegrityError:\n"
                            f"            self.fail('{model_name}.{field.name} OneToOneField creation failed')\n"
                            f"\n"
                        )
                    elif isinstance(field, models.ManyToManyField):
                        related_model = field.related_model.__name__
                        test_cases.append(
                            f"    def test_{model_name.lower()}_{field.name}_many_to_many_field(self):\n"
                            f"        \"\"\"Test {model_name}.{field.name} ManyToManyField to {related_model}\"\"\"\n"
                            f"        try:\n"
                            f"            obj = {model_name}.objects.create()\n"
                            f"            related_obj = {related_model}.objects.create()\n"
                            f"            obj.{field.name}.add(related_obj)\n"
                            f"            self.assertIn(related_obj, obj.{field.name}.all())\n"
                            f"        except IntegrityError:\n"
                            f"            self.fail('{model_name}.{field.name} ManyToManyField creation failed')\n"
                            f"\n"
                        )

    return "\n".join(test_cases)


def main():
    """Generate tests for all associations and save them to a file."""
    test_code = get_association_tests()
    with open(TEST_FILE_PATH, "w") as test_file:
        test_file.write(test_code)
    print(f"Generated association tests in {TEST_FILE_PATH}")


if __name__ == "__main__":
    main()
