"""
Apps configuration for grocery app
Author: Priyanshu Verma
"""

from django.apps import AppConfig


class GroceryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grocery'
    verbose_name = 'Grocery Items'
