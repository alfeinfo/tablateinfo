from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tablate',
        'USER': 'postgres',
        'PASSWORD': 'alfeinfo',
        'HOST':  'localhost',
        'PORT': '5432',
    }
}