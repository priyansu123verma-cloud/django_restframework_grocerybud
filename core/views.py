"""
Views for core app.
Author: Priyanshu Verma
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HelloWorldView(APIView):
    """Hello World API endpoint"""
    
    def get(self, request):
        """Return hello world message"""
        return Response({
            'message': 'Hello from GroceryBud API',
            'author': 'Priyanshu Verma',
            'version': '1.0.0'
        }, status=status.HTTP_200_OK)
