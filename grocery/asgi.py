"""
ASGI config for GroceryBud project.
Author: Priyanshu Verma
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
