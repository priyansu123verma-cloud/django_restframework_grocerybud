# Backend Configuration

This directory contains Django REST Framework backend configuration.

**Author:** Priyanshu Verma

## API Endpoints

- `GET /api/items/` - List all grocery items
- `POST /api/items/` - Create a new grocery item
- `GET /api/items/{id}/` - Get a specific item
- `PUT /api/items/{id}/` - Update an item
- `DELETE /api/items/{id}/` - Delete an item
- `POST /api/items/{id}/mark_purchased/` - Mark item as purchased
- `POST /api/items/{id}/mark_unpurchased/` - Mark item as unpurchased
- `GET /api/items/purchased/` - Get all purchased items
- `GET /api/items/unpurchased/` - Get all unpurchased items
