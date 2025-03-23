from .base import *

DEBUG=True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": os.environ.get('PROD_DB_USER_NAME'),
        "NAME": os.environ.get('PROD_DB_NAME'),
        "PASSWORD": os.environ.get('PROD_DB_PASSWORD'),
        "HOST": os.environ.get('PROD_DB_HOST'),
        "PORT": os.environ.get('PROD_DB_PORT',"3306"),
    }
}
ALLOWED_HOSTS = [os.getenv('PROD_ALLOWED_HOST', '')]
AWS_ACCESS_KEY_ID = os.environ.get('PROD_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('PROD_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('PROD_AWS_STORAGE_BUCKET_NAME')
MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/"
STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"
STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "bucket_name": AWS_STORAGE_BUCKET_NAME,
                "location": 'media'
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "bucket_name": AWS_STORAGE_BUCKET_NAME,
                "location": 'static'
            },
        },
    }

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django-app.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}