# Setup Guide - GroceryBud

**Author:** Priyanshu Verma

Complete setup instructions for running the GroceryBud application locally.

## Prerequisites

- Python 3.9 or higher
- Node.js 14 or higher
- pip and npm package managers

## Backend Setup

### 1. Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
```

### 4. Database Setup

```bash
# Create database tables
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
# Follow prompts to create admin account
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Backend will be available at: `http://localhost:8000`

**Admin Panel:** `http://localhost:8000/admin/`
**API Documentation:** `http://localhost:8000/api/`

## Frontend Setup

### 1. Navigate to Frontend Directory

```bash
cd grocery-bud-react
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start Development Server

```bash
npm run dev
```

Frontend will open automatically at: `http://localhost:5173`

## API Endpoints

All endpoints are available at `http://localhost:8000/api/`

### Grocery Items

- `GET /items/` - List all items
- `POST /items/` - Create new item
- `GET /items/{id}/` - Get specific item
- `PUT /items/{id}/` - Update item
- `PATCH /items/{id}/` - Partial update
- `DELETE /items/{id}/` - Delete item
- `POST /items/mark_purchased/` - Mark items as purchased
- `GET /items/stats/` - Get statistics

## Common Commands

### Backend

```bash
# Run tests
python manage.py test

# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Open Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

### Frontend

```bash
# Development mode with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Troubleshooting

### Django Issues

**Database errors:**
```bash
# Reset database (development only!)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

**Module not found:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### React Issues

**Port already in use:**
```bash
# Edit vite.config.js to use different port
server: {
  port: 5174,
}
```

**Module errors:**
```bash
# Clear node_modules and reinstall
rm -rf node_modules
npm install
```

## Project Structure

```
GroceryBud/
├── api/                    # Django app for API
├── backend/                # Django project configuration
├── grocery-bud-react/      # React frontend
├── db.sqlite3              # Database file
├── manage.py               # Django CLI
├── requirements.txt        # Python dependencies
└── .env                   # Environment variables
```

## API Request Examples

### Create Item

```bash
curl -X POST http://localhost:8000/api/items/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Milk",
    "quantity": "1 Liter"
  }'
```

### Get Statistics

```bash
curl http://localhost:8000/api/items/stats/
```

### Mark Items as Purchased

```bash
curl -X POST http://localhost:8000/api/items/mark_purchased/ \
  -H "Content-Type: application/json" \
  -d '{
    "ids": [1, 2, 3]
  }'
```

## Database

- **Development:** SQLite (`db.sqlite3`)
- **Production:** PostgreSQL (recommended)

### Backup Database

```bash
# Copy the db.sqlite3 file
cp db.sqlite3 db.sqlite3.backup
```

## Performance Tips

1. Use pagination for large datasets
2. Add indexes on frequently queried fields
3. Implement caching for statistics
4. Minify frontend assets for production

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)

## Contact

**Author:** Priyanshu Verma

For support or questions, please open an issue or contact the author.
