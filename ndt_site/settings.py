"""
Django settings for ndt_site project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json


try:
    with open("/etc/config.json") as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    pass


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

try:
    SECRET_KEY = config["SECRET_KEY"]
except NameError:
    pass
# SECURITY WARNING: don't run with debug turned on in production!
try:
    GET_DEBUG = config.get("DEBUG")

    if GET_DEBUG == 'True':
        DEBUG = True
    else:
        DEBUG = False
except NameError:
    DEBUG = True
    



ALLOWED_HOSTS = ['104.237.143.152', 'localhost', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'towers.apps.TowersConfig',
    'blogs.apps.BlogsConfig',
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phone_field',
    'django.contrib.humanize',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ndt_site.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ndt_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


try:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config["DB_NAME"],
            'USER': config["DB_USER"],
            'PASSWORD': config["DB_PASSWORD"],
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
except NameError:
    pass

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Countries module settings
COUNTRIES_FIRST =  [
    'US',
    'GB',
]



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/




################# AWS ACCESS KEYS
try:
    AWS_ACCESS_KEY_ID = config.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config.get("AWS_STORAGE_BUCKET_NAME")

    AWS_LOCATION = 'static'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.us-east-2.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
except NameError:
    pass



# when collectstatic runs this it will collect all static files and put them here
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

try:
    from .local_settings import *
except ImportError:
    pass