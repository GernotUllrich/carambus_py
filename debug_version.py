import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carambus_py.settings')
django.setup()

from carambus_py.models import Version

# Call the class method you want to debug
Version.update_carambus()
