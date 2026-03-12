"""
Tests for grocery app
Author: Priyanshu Verma
"""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import GroceryItem


class GroceryItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = GroceryItem.objects.create(
            name='Test Item',
            quantity='5 pieces',
            purchased=False
        )

    def test_list_grocery_items(self):
        """Test listing grocery items"""
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_grocery_item(self):
        """Test creating a new grocery item"""
        data = {
            'name': 'Milk',
            'quantity': '1 Liter'
        }
        response = self.client.post('/api/items/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)

    def test_update_grocery_item(self):
        """Test updating a grocery item"""
        data = {
            'name': 'Updated Item',
            'quantity': '10 pieces'
        }
        response = self.client.put(f'/api/items/{self.item.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')

    def test_delete_grocery_item(self):
        """Test deleting a grocery item"""
        response = self.client.delete(f'/api/items/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(GroceryItem.objects.count(), 0)

    def test_mark_purchased(self):
        """Test marking items as purchased"""
        response = self.client.post('/api/items/mark_purchased/', {'ids': [self.item.id]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertTrue(self.item.purchased)

    def test_get_stats(self):
        """Test getting grocery statistics"""
        response = self.client.get('/api/items/stats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_items', response.data)
        self.assertIn('purchased_items', response.data)
        self.assertIn('pending_items', response.data)

    def test_validation_empty_name(self):
        """Test validation for empty name"""
        data = {
            'name': '',
            'quantity': '5'
        }
        response = self.client.post('/api/items/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validation_name_too_short(self):
        """Test validation for name too short"""
        data = {
            'name': 'A',
            'quantity': '5'
        }
        response = self.client.post('/api/items/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
