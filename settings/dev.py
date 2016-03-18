from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'example.sqlite',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sentry.db',
        'USER': 'wanghe',
        'PASSWORD': 'yuxuangh',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
