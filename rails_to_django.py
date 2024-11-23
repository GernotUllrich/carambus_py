import os
import re

# Pfade anpassen
RAILS_MODELS_DIR = "rails_models/"  # Verzeichnis mit Rails-Modellen (*.rb)
DJANGO_MODELS_DIR = "rails_models/"  # Zielverzeichnis für Django-Modelle

# Stelle sicher, dass das Zielverzeichnis existiert
os.makedirs(DJANGO_MODELS_DIR, exist_ok=True)


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
    """Erstellt eine Django-Modell-Klasse basierend auf den geparsten Daten."""
    model_name = parsed_model["model_name"]
    fields = parsed_model["fields"]
    associations = parsed_model["associations"]

    lines = [f"from django.db import rails_models\n\n\nclass {model_name}(rails_models.Model):"]

    # Füge Felder hinzu
    for field in fields:
        field_type = map_field_type(field["type"])
        lines.append(f"    {field['name']} = rails_models.{field_type}")

    # Füge Assoziationen hinzu
    for assoc_type, assoc_name in associations:
        if assoc_type == "belongs_to":
            lines.append(f"    {assoc_name} = rails_models.ForeignKey('{assoc_name.capitalize()}', on_delete=rails_models.CASCADE)")
        elif assoc_type == "has_many":
            # Hinweise für eine separate Implementierung
            lines.append(
                f"    # {assoc_name} = rails_models.RelatedField('{assoc_name.capitalize()}', related_name='{model_name.lower()}')")
        elif assoc_type == "has_one":
            lines.append(
                f"    {assoc_name} = rails_models.OneToOneField('{assoc_name.capitalize()}', on_delete=rails_models.CASCADE)")

    # Meta-Klasse
    lines.append("\n    class Meta:")
    lines.append(f"        db_table = '{model_name.lower()}'")

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
    return mapping.get(rails_type, "TextField()")  # Standardmäßig TextField()


def main():
    # Iteriere durch alle Rails-Modelldateien
    for file_name in os.listdir(RAILS_MODELS_DIR):
        if file_name.endswith(".rb"):
            file_path = os.path.join(RAILS_MODELS_DIR, file_name)
            parsed_model = parse_rails_model(file_path)

            if parsed_model["model_name"]:
                # Generiere Django-Modell
                django_model = generate_django_model(parsed_model)

                # Schreibe die Django-Modell-Datei
                django_file_path = os.path.join(DJANGO_MODELS_DIR, f"{parsed_model['model_name'].lower()}.py")
                with open(django_file_path, 'w') as django_file:
                    django_file.write(django_model)
                print(f"Generiert: {django_file_path}")


if __name__ == "__main__":
    main()
