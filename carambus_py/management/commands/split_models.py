import os
import re
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Splits the models.py file into separate files for each model with optimized imports and cleaned definitions."

    def handle(self, *args, **options):
        app_name = "carambus_py"  # Replace with your app's name
        app_dir = os.path.join(os.getcwd(), app_name)
        models_file = os.path.join(app_dir, "models.py")
        output_dir = os.path.join(app_dir, "models")

        if not os.path.exists(models_file):
            self.stderr.write(f"models.py not found in {app_name}.")
            return

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Load the models.py content
        with open(models_file, "r") as file:
            content = file.read()

        # Regular expression to match model definitions
        model_regex = r"(?s)(class\s+\w+\(models\.Model\):.*?)(?=\nclass\s+\w+\(models\.Model\):|\Z)"
        models = re.findall(model_regex, content)

        if not models:
            self.stderr.write("No models found in models.py. Please check the file format.")
            return

        self.stdout.write(f"Found {len(models)} models in models.py.")

        # Process each model
        for model in models:
            # Extract the model name
            model_name_match = re.search(r"class\s+(\w+)", model)
            if not model_name_match:
                self.stderr.write("Could not determine the model name for one of the matches.")
                continue
            model_name = model_name_match.group(1)
            model_filename = self.to_snake_case(model_name)
            model_file = os.path.join(output_dir, f"{model_filename}.py")

            # Convert ForeignKey and other relations to class-based references
            model = self.convert_foreign_keys(model)

            # Analyze the model for needed imports
            required_imports = self.get_required_imports(model)

            # Write the model file
            with open(model_file, "w") as model_file_obj:
                model_file_obj.write("\n".join(required_imports) + "\n\n" + model.strip())
            self.stdout.write(f"Model {model_name} saved to {model_file}")

        # Create or update __init__.py in the models directory
        init_file = os.path.join(output_dir, "__init__.py")
        with open(init_file, "w") as init_file_obj:
            for model in models:
                model_name_match = re.search(r"class\s+(\w+)", model)
                if model_name_match:
                    model_filename = self.to_snake_case(model_name_match.group(1))
                    init_file_obj.write(f"from .{model_filename} import {model_name_match.group(1)}\n")
        self.stdout.write("Updated __init__.py in models directory.")

    def convert_foreign_keys(self, model):
        """
        Replace string-based references in ForeignKey, OneToOneField, and ManyToManyField with class references,
        excluding GenericForeignKey and models.ForeignKey(ContentType, ...).
        """
        # Match fields with string-based references but exclude GenericForeignKey and ContentType ForeignKey
        relation_regex = re.compile(
            r"(?<!Generic)(ForeignKey|OneToOneField|ManyToManyField)\(\s*['\"](\w+)['\"]"
        )
        content_type_regex = re.compile(
            r"models\.ForeignKey\(\s*ContentType\s*,.*?\)"
        )

        # Convert ForeignKey string references to class references
        updated_model = relation_regex.sub(r"\1(\2", model)

        # Ensure models.ForeignKey(ContentType, ...) is untouched
        updated_model = content_type_regex.sub(r"models.ForeignKey(ContentType, on_delete=models.CASCADE)", updated_model)

        return updated_model

    def get_required_imports(self, model):
        """
        Analyze the model and determine the required imports based on its usage.
        """
        imports = set()

        # Base import for Django models
        imports.add("from django.db import models")

        # Add imports for common Django fields or related classes
        if "GenericForeignKey" in model:
            imports.add("from django.contrib.contenttypes.fields import GenericForeignKey")
        if "ContentType" in model and "models.ForeignKey(ContentType" not in model:
            imports.add("from django.contrib.contenttypes.models import ContentType")
        if "F(" in model:
            imports.add("from django.db.models import F")

        # Add imports for any related models, except ContentType
        related_model_pattern = re.compile(r"(ForeignKey|OneToOneField|ManyToManyField)\(\s*(\w+)")
        for match in related_model_pattern.findall(model):
            related_model_name = match[1]
            if related_model_name != "ContentType":  # Skip ContentType
                imports.add(f"from .{self.to_snake_case(related_model_name)} import {related_model_name}")

        return sorted(imports)

    def to_snake_case(self, name):
        """
        Convert CamelCase or PascalCase to snake_case.
        """
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
