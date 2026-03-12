"""
GroceryBud Django Models
Author: Priyanshu Verma
"""

from django.db import models


class GroceryItem(models.Model):
    """Model for grocery items"""
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Grocery Items'

    def __str__(self):
        return self.name
