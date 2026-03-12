"""
Tests for core app
Author: Priyanshu Verma
"""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class HelloWorldTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_hello_world_endpoint(self):
        """Test that hello world endpoint returns correct message"""
        response = self.client.get('/api/hello/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['author'], 'Priyanshu Verma')
