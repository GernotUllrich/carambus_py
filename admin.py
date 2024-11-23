from django.contrib import admin
from django.apps import apps

# Get the current app's label (e.g., 'my_app')
current_app_label = __name__.split('.')[0]

# Register rails_models belonging only to the current app
app = apps.get_app_config(current_app_label)

for model in app.get_models():
    if model._meta.app_label == current_app_label:  # Ensure the model is part of the current app
        admin.site.register(model)
