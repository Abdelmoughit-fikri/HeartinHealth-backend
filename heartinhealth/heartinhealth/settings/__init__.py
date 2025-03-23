# settings/__init__.py
import os
from .base import *

# Check for environment variable to determine which settings to use
env = os.environ.get('DJANGO_ENV', 'production')

if env == 'development':
    from .dev import *
else:
    from .prod import *