from .base import *
from dotenv import load_dotenv
load_dotenv()

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




# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 86400
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
