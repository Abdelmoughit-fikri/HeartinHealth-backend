from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": os.environ.get('DB_USER_NAME'),
        "NAME": os.environ.get('DB_NAME'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "HOST": os.environ.get('PROD_DB_HOST'),
        "PORT": os.environ.get('PROD_DB_PORT'),
    }
}
ALLOWED_HOSTS = [os.getenv('PROD_ALLOWED_HOST', '')]
AWS_ACCESS_KEY_ID = os.environ.get('PROD_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('PROD_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('PROD_AWS_STORAGE_BUCKET_NAME')