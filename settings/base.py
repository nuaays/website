# Django settings for example project.
import os
from os.path import join, abspath, dirname

import django.conf.global_settings as DEFAULT_SETTINGS

# Root directory of our project
PROJECT_ROOT = abspath(join(abspath(dirname(__file__)), "..",))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = os.environ.get('DJANGO_DEBUG', True)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {}

MANAGERS = ADMINS

MAX_SENTRY_INSTANCE_COUNT = 20
DEFAULT_SUB_DOMAIN_SUFFIX = ".loginsight.cn"
SENTRY_API = "http://localhost:9000/api/0"

# aliyun secret key
ALIYUN_ACCESS_KEY_ID = "7DifeHNHQxe5IIW5"
ALIYUN_ACCESS_KEY_SECRET = "tJhvPpv4In1oeuSU79dtZcBAGHisPs"
ALIYUN_ECS_REGIONID = 'cn-qingdao'
ALIYUN_ECS_SENTRY_INSTANCE_PREFIX = "sentry"
SENTRY_DEFALUT_PORT = "8000"
OFFICIAL_DOMAIN_NAME = "loginsight.cn"

# vhost for nginx conf
NGINX_VHOST_CONF_DIR = "/usr/local/etc/nginx/site-enabled/"

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATIC_ROOT = join(PROJECT_ROOT, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'do_not_use_this_key')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',

)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)


AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    'django.contrib.auth.backends.ModelBackend'
)

REST_FRAMEWORK = {
    # ...

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',

    )
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'example.middleware.XsSharingMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "example.context_processors.dot_version",
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'oauth2_provider',
    'south',
    'example',
    'website',
    'corsheaders',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'oauth2_provider': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'oauthlib': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}


OAUTH2_PROVIDER = {
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'APPLICATION_MODEL': 'example.MyApplication',
    'REQUEST_APPROVAL_PROMPT': 'auto',
}


CLIENT_ID='L_Ja%21V13e%218pWJpWP%3FPE-metmZ%3FS0%3Bs%213XHgu%3Bok'
CLIENT_SECRET=''
OAUTH_SERVER="http://localhost:8000"


from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('index')

USERS_REGISTRATION_OPEN = True
 
USERS_VERIFY_EMAIL = True
  
USERS_AUTO_LOGIN_ON_ACTIVATION = True
   
USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3
    
# Specifies minimum length for passwords:
USERS_PASSWORD_MIN_LENGTH = 5
     
# Specifies maximum length for passwords:
USERS_PASSWORD_MAX_LENGTH = None
      
# the complexity validator, checks the password strength
USERS_CHECK_PASSWORD_COMPLEXITY = True
       
USERS_SPAM_PROTECTION = False  # important!

ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='localhost'
EMAIL_PORT=465
EMAIL_HOST_USER='wangh@loginsight.cn'
EMAIL_HOST_PASSOWORD='wh@yuxuangh&163'
EMAIL_USE_TLS=False
DEFAULT_FORM_EMAIL='wangh@loginsight.cn'

