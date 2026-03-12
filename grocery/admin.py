"""
Admin configuration for GroceryBud
Author: Priyanshu Verma
"""

from django.contrib import admin
from .models import GroceryItem


@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'purchased', 'created_at')
    list_filter = ('purchased', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Item Information', {
            'fields': ('name', 'quantity', 'purchased')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
