"""
Django settings for deposito project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# new - LDAP authentications
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

# store secrets in another file
from deposito.secret_settings import *

from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APPEND_SLASH = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar', #refer to https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    'private_storage', #refer to https://github.com/edoburu/django-private-storage
    'envio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', # for debug purposes.
]

ROOT_URLCONF = 'deposito.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # To access the MEDIA_URL in templates
            ],
        },
    },
]

WSGI_APPLICATION = 'deposito.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# New authentication backend.
# first install python-ldap and django-auth-ldap
AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Baseline configuration for LDAP
AUTH_LDAP_SERVER_URI = 'ldap://ldapmail.unizar.es:389'
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 1,
    #ldap.OPT_REFERRALS: 1,
}

#AUTH_LDAP_USER_SEARCH = LDAPSearch(
#    'ou=Accounts,dc=unizar,dc=es',
#    ldap.SCOPE_SUBTREE,
#    '(uid=%(user)s)',
#)
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=Accounts,dc=unizar,dc=es"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn', #FIXME
    'email': 'mail',
}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# unizar ldap not via TLS, plain. port 389
AUTH_LDAP_START_TLS = False

# UNIZAR LDAP WORKS LIKE A DIRECT BIND, SO NO AUTH_LDAP_USER_SEARCH_NEEDED
# In order to check if the connection works, try ldapsearch first...
# ldapsearch -L -h ldapmail.unizar.es -p 389 -D 'uid=AQUIELUID,ou=Accounts,dc=unizar,dc=es' -w AQUIELPASSWORD -b 'dc=unizar,dc=es' -s sub "uid=AQUIELUID"


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# limit languages to english and spanish
LANGUAGES = (
 ('en', _('English')),
 ('es', _('Spanish')),
)

LOCALE_PATHS = ( os.path.join(os.path.dirname(__file__), 'envio/locale'), )

LANGUAGE_CODE = 'es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

LOGOUT_REDIRECT_URL = 'index'
LOGIN_REDIRECT_URL = 'index'

INTERNAL_IPS = ['127.0.0.1']

# Media uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# For private storage. Refer to https://github.com/edoburu/django-private-storage
PRIVATE_STORAGE_ROOT = 'private-media/'
PRIVATE_STORAGE_AUTH_FUNCTION = 'private_storage.permissions.allow_staff'

# Set message level to DEBUG
MESSAGE_LEVEL = 10  # DEBUG (refer to https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html)
