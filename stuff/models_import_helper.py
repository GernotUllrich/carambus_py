# your_project/tests/utils/models_import_helper.py
from django.apps import apps


def import_all_models():
    """
       Dynamically imports all models_xxx from installed apps.
       """
    all_models = {}
    for app_config in apps.get_app_configs():
        app_models = app_config.get_models()
        for model in app_models:
            model_label = f"{model._meta.app_label}.{model._meta.model_name}"
            all_models[model_label] = model
    return all_models