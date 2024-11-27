from .settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carambus_py_local_test_db',  # Name of your test database
        'USER': '',    # Replace with your PostgreSQL username
        'PASSWORD': '', # Replace with your PostgreSQL password
        'HOST': 'localhost',        # Or the IP of your PostgreSQL server
        'PORT': '5432',             # Default PostgreSQL port
    }
}

