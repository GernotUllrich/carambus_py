import os
import re
import inflect
import inflection  # For camelize and underscore

# Initialize the inflect engine
inflect_engine = inflect.engine()

RAILS_MODELS_DIR = "rails_models/"  # Verzeichnis mit Rails-Modellen (*.rb)
DJANGO_MODELS_DIR = "carambus_py/models/"  # Zielverzeichnis für Django-Modelle
DJANGO_EXISTING_MODELS_FILE = "carambus_py/models.py"  # Generierte rails_models.py von Django

os.makedirs(DJANGO_MODELS_DIR, exist_ok=True)


def parse_existing_django_models(file_path):
    """Extrahiert die Tabellen-/Modellnamen aus der generierten Django rails_models.py."""
    with open(file_path, 'r') as file:
        content = file.read()
    # Suche nach Klassennamen in der Form `class ModelName(rails_models.Model):`
    matches = re.findall(r"class (\w+)\(rails_models\.Model\):", content)
    return set(matches)  # Rückgabe als Set für schnelles Nachschlagen


def parse_rails_model(file_path):
    """Parsiert ein Rails-Model, um den Modellnamen, Felder und Assoziationen zu extrahieren."""
    with open(file_path, 'r') as file:
        content = file.read()

    # Extrahiere den Modellnamen
    model_name_match = re.search(r"class (\w+) < ApplicationRecord", content)
    model_name = model_name_match.group(1) if model_name_match else None

    # Extrahiere Felder
    field_matches = re.findall(r"t\.(\w+)\s+\"(\w+)\"", content)
    fields = [{"type": f[0], "name": f[1]} for f in field_matches]

    # Extrahiere Assoziationen
    associations = re.findall(r"(belongs_to|has_many|has_one) :(\w+)", content)

    return {
        "model_name": model_name,
        "fields": fields,
        "associations": associations
    }

def generate_django_model(parsed_model):
    """Generates a Django model class based on the parsed Rails model."""
    model_name = parsed_model["model_name"]
    fields = parsed_model["fields"]
    associations = parsed_model["associations"]

    lines = [f"from django.db import rails_models\n\n\nclass {model_name}(rails_models.Model):"]

    for field in fields:
        field_type = map_field_type(field["type"])
        lines.append(f"    {field['name']} = rails_models.{field_type}")

    for assoc_type, assoc_name in associations:
        if assoc_type == "belongs_to":
            lines.append(f"    {assoc_name} = rails_models.ForeignKey('{inflection.camelize(assoc_name)}', on_delete=rails_models.CASCADE)")
        elif assoc_type == "has_many":
            lines.append(f"    # {assoc_name} = rails_models.RelatedField('{inflection.camelize(assoc_name)}', related_name='{model_name.lower()}')")
        elif assoc_type == "has_one":
            lines.append(f"    {assoc_name} = rails_models.OneToOneField('{inflection.camelize(assoc_name)}', on_delete=rails_models.CASCADE)")

    # Use pluralized and underscored table name for db_table
    table_name = inflection.pluralize(inflection.underscore(model_name))
    lines.append("\n    class Meta:")
    lines.append(f"        db_table = '{table_name}'")

    return "\n".join(lines)




def map_field_type(rails_type):
    """Mappt Rails-Feldtypen auf Django-Feldtypen."""
    mapping = {
        "string": "CharField(max_length=255)",
        "text": "TextField()",
        "integer": "IntegerField()",
        "boolean": "BooleanField()",
        "datetime": "DateTimeField()",
        "decimal": "DecimalField(max_digits=10, decimal_places=2)",
    }
    return mapping.get(rails_type, "TextField()")


def generate_init_file(django_models_dir, model_files):
    """Generiert die __init__.py-Datei, die alle Modelle importiert."""
    init_file_path = os.path.join(django_models_dir, "__init__.py")
    with open(init_file_path, "w") as init_file:
        for model_file in model_files:
            model_name = os.path.splitext(model_file)[0]
            init_file.write(f"from .{model_name} import {inflection.camelize(model_name)}\n")
    print(f"Generated: {init_file_path}")


def main():
    # Extrahiere bestehende Modelle aus rails_models.py
    existing_models = parse_existing_django_models(DJANGO_EXISTING_MODELS_FILE)

    # Konvertiere bestehende Modelle zu Singularformen und unterstreiche für den Vergleich
    normalized_existing_models = {
        inflection.underscore(inflect_engine.singular_noun(model) or model).lower()
        for model in existing_models
    }

    model_files = []  # List to store generated model file names

    # Iteriere durch alle Rails-Modelldateien
    for file_name in os.listdir(RAILS_MODELS_DIR):
        if file_name.endswith(".rb"):
            file_path = os.path.join(RAILS_MODELS_DIR, file_name)
            parsed_model = parse_rails_model(file_path)

            # Normalisiere den Modellnamen für Rails
            if parsed_model["model_name"]:
                normalized_model_name = inflection.underscore(parsed_model["model_name"]).lower()

                # Überprüfen, ob das Rails-Modell in den Django-Modellen enthalten ist
                if normalized_model_name in normalized_existing_models:
                    django_model = generate_django_model(parsed_model)
                    django_file_name = f"{normalized_model_name}.py"
                    django_file_path = os.path.join(DJANGO_MODELS_DIR, django_file_name)

                    # Schreibe das Modell in eine Datei
                    with open(django_file_path, 'w') as django_file:
                        django_file.write(django_model)
                    model_files.append(django_file_name)
                    print(f"Generated: {django_file_path}")
                else:
                    print(f"Skipped: {file_name} (not found in rails_models.py)")

    # Generiere die __init__.py-Datei
    generate_init_file(DJANGO_MODELS_DIR, model_files)


if __name__ == "__main__":
    main()
