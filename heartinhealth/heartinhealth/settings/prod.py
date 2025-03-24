from .base import *
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": os.getenv('PROD_DB_USER_NAME'),
        "NAME": os.getenv('PROD_DB_NAME'),
        "PASSWORD": os.getenv('PROD_DB_PASSWORD'),
        "HOST": os.getenv('PROD_DB_HOST'),
        "PORT": os.getenv('PROD_DB_PORT',"3306"),
    }
}
}
# ALLOWED_HOSTS = [os.getenv('PROD_ALLOWED_HOSTS', '')]
# ALLOWED_HOSTS = ['51.21.200.11']
# AWS_ACCESS_KEY_ID = os.getenv('PROD_AWS_ACCESS_KEY_ID')
AWS_ACCESS_KEY_ID = 'AKIAXZEFIEOT7SCT4NVW'
# AWS_SECRET_ACCESS_KEY = os.getenv('PROD_AWS_SECRET_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = os.getenv('PROD_AWS_STORAGE_BUCKET_NAME')
AWS_STORAGE_BUCKET_NAME = 'heartinhealth'
MEDIA_URL = "https://heartinhealth.s3.amazonaws.com/media/"
STATIC_URL = "https://heartinhealth.s3.amazonaws.com/static/"
STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "bucket_name": 'heartinhealth',
                "location": 'media'
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "bucket_name": 'heartinhealth',
                "location": 'static'
            },
        },
    }





# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 86400
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
