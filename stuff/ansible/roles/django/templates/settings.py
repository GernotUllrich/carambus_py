DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'carambus_py_local',
         'USER': '{{ database_user }}',
         'PASSWORD': '{{ database_password }}',
         'HOST': 'localhost',
         'PORT': '5432',
     },
     'api': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'carambus_py_api',
         'USER': '{{ database_user }}',
         'PASSWORD': '{{ database_password }}',
         'HOST': 'localhost',
         'PORT': '5432',
     },
}

# Other Django settings
