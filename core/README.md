# Core App - GroceryBud Core API

This is the core application containing basic API endpoints.

**Author:** Priyanshu Verma

## Functionality

### HelloWorld Endpoint
A simple endpoint to verify that the Django REST Framework API is running correctly.

**Endpoint:** `GET /api/hello/`

**Response:**
```json
{
  "message": "Hello from GroceryBud API",
  "author": "Priyanshu Verma",
  "version": "1.0.0"
}
```

## Use Cases

- Health check endpoint
- API availability verification
- Basic integration testing
- API version checking

## Files

- `views.py` - Contains HelloWorldView
- `urls.py` - URL routing
- `serializers.py` - DRF serializers (if needed)
- `models.py` - Base model configuration
- `admin.py` - Django admin configuration
- `apps.py` - App configuration
- `tests.py` - Unit tests

## Testing

Run tests with:
```bash
python manage.py test core
```
