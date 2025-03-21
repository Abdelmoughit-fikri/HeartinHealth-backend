import os
from pathlib import Path

import os

BASE_DIR = Path(__file__).resolve().parent.parent

from dotenv import load_dotenv
load_dotenv()



DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cardiacWellBeing",
    "cardiacDiseases",
    "cardiacSymptomsAndDiagnosis",
    "cardiacInnovations",
    "search",
    "rest_framework",
    "drf_spectacular",
    'storages',
    "corsheaders",
    'django_ckeditor_5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "heartinhealth.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    'http://192.168.1.110:3000'
]

CORS_ALLOW_METHODS = [
    "GET",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = [
    "Content-Type",
]

WSGI_APPLICATION = "heartinhealth.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": os.environ.get('DB_USER_NAME'),
        "NAME": os.environ.get('DB_NAME'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": os.environ.get('DB_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID_ENV')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY_ENV')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME_ENV')
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "custom_domain": "heartinhealth.s3.amazonaws.com",
        }
    },
}

MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/"
STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', 'bold', 'italic', 'link', 'emoji', 'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', '|', 'outdent', 'indent', 'link'
        ],
        'language': 'en',
    },
}
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"

SECRET_KEY = os.environ.get('PROJECT_SECRET_KEY_ENV')
