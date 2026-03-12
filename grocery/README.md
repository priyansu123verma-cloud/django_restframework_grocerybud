# Grocery App - Django Application

This is the main Django app for managing grocery items.

**Author:** Priyanshu Verma

## Features

- CRUD operations for grocery items
- Mark items as purchased/unpurchased
- Filter by category
- Price tracking
- Quantity management

## Models

### GroceryItem
- `name` - Name of the item
- `description` - Item description
- `quantity` - Quantity of item
- `price` - Price of item
- `category` - Item category
- `is_purchased` - Purchase status
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

## API Endpoints

- `GET /api/grocery-items/` - List all items
- `POST /api/grocery-items/` - Create new item
- `GET /api/grocery-items/{id}/` - Get specific item
- `PUT /api/grocery-items/{id}/` - Update item
- `DELETE /api/grocery-items/{id}/` - Delete item
- `POST /api/grocery-items/{id}/mark_purchased/` - Mark as purchased
- `POST /api/grocery-items/{id}/mark_unpurchased/` - Mark as unpurchased
- `GET /api/grocery-items/purchased/` - Get purchased items
- `GET /api/grocery-items/unpurchased/` - Get unpurchased items

## Admin Interface

Access Django admin at `/admin/` to manage grocery items directly.
