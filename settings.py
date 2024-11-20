DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carambus_py_local',
        'USER': '',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'api': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carambus_py_api',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

