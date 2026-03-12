"""
DRF Serializers for GroceryBud
Author: Priyanshu Verma
"""

from rest_framework import serializers
from .models import GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):
    """Serializer for GroceryItem model"""
    
    class Meta:
        model = GroceryItem
        fields = ['id', 'name', 'quantity', 'purchased', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_name(self, value):
        """Validate name field"""
        if not value or value.strip() == '':
            raise serializers.ValidationError("Item name cannot be empty")
        if len(value) < 2:
            raise serializers.ValidationError("Item name must be at least 2 characters long")
        if len(value) > 100:
            raise serializers.ValidationError("Item name cannot exceed 100 characters")
        return value.strip()

    def validate_quantity(self, value):
        """Validate quantity field"""
        if not value or value.strip() == '':
            raise serializers.ValidationError("Quantity cannot be empty")
        return value.strip()

    def validate(self, data):
        """Cross-field validation"""
        if data.get('name') and data.get('quantity'):
            pass
        return data
