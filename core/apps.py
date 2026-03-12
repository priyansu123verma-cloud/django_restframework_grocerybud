"""
Apps configuration for GroceryBud
Author: Priyanshu Verma
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Core App'
