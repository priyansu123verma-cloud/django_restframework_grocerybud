"""
Core app for GroceryBud project.
Author: Priyanshu Verma

This app contains core functionality and hello world API.
"""

from django.db import models


class CoreModel(models.Model):
    """Base model for core functionality"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
