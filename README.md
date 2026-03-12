# CRUD with Django REST Framework and React

A full-stack grocery management application built with Django REST Framework and React with Vite.

**Author:** Priyanshu Verma

## 📋 Overview

This project demonstrates CRUD (Create, Read, Update, Delete) operations using Django REST Framework for the backend and React for the frontend. It allows users to manage their grocery shopping lists efficiently.

### Tech Stack

- **Backend:** Django 6.0+, Django REST Framework
- **Frontend:** React 18.2+, Vite, Axios
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Styling:** Custom CSS

## 📁 Project Structure

```
GroceryBud/
├── api/                       # Django API app
│   ├── models.py             # GroceryItem model
│   ├── serializers.py        # DRF serializers with validation
│   ├── views.py              # Viewsets with custom endpoints
│   ├── urls.py               # API URL routing
│   ├── admin.py              # Django admin configuration
│   └── migrations/           # Database migrations
│
├── backend/                   # Django project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py               # WSGI application
│   ├── asgi.py               # ASGI application
│   └── __init__.py
│
├── grocery-bud-react/        # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx           # Main React component
│   │   ├── index.js          # React entry point
│   │   ├── services/
│   │   │   └── api.js        # Axios API client
│   │   └── styles/
│   │       ├── App.css       # App styles
│   │       └── index.css     # Global styles
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── .gitignore
│
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 14+
- pip and npm

### Backend Setup

1. **Navigate to project directory:**
   ```bash
   cd GroceryBud
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server:**
   ```bash
   python manage.py runserver
   ```

   Backend runs at: `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd grocery-bud-react
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

   Frontend runs at: `http://localhost:5173`

## 📚 API Endpoints

### Grocery Items API

- **GET** `/api/items/` - List all items
- **POST** `/api/items/` - Create new item
- **GET** `/api/items/{id}/` - Get specific item
- **PUT** `/api/items/{id}/` - Update item
- **PATCH** `/api/items/{id}/` - Partial update
- **DELETE** `/api/items/{id}/` - Delete item
- **POST** `/api/items/mark_purchased/` - Mark multiple items as purchased
- **GET** `/api/items/stats/` - Get grocery statistics

### Request/Response Examples

**Create Item:**
```json
POST /api/items/
{
  "name": "Milk",
  "quantity": "1 Liter"
}

Response:
{
  "message": "Grocery item created successfully",
  "data": {
    "id": 1,
    "name": "Milk",
    "quantity": "1 Liter",
    "purchased": false,
    "created_at": "2026-03-12T10:30:00Z"
  }
}
```

**Get Statistics:**
```json
GET /api/items/stats/

Response:
{
  "total_items": 5,
  "purchased_items": 2,
  "pending_items": 3
}
```

## 🎨 Database Model

### GroceryItem Model

```python
{
  "id": {type: "BigAutoField", primary: true},
  "name": {type: "CharField", max_length: 100},
  "quantity": {type: "CharField", max_length: 50},
  "purchased": {type: "BooleanField", default: false},
  "created_at": {type: "DateTimeField", auto_now_add: true}
}
```

## 🔧 Features

### Backend
- RESTful API with Django REST Framework
- Complete CRUD operations
- Custom model validation
- Error handling with meaningful messages
- Admin interface for data management
- CORS support for all origins
- Statistics endpoint

### Frontend
- Modern React UI with Vite
- Add, edit, and delete items
- Mark items as purchased/unpurchased
- Real-time statistics display
- Error handling and loading states
- Responsive design
- Axios for API communication

## 📦 Dependencies

### Backend (`requirements.txt`)
```
Django==4.1.7
djangorestframework==3.14.0
django-cors-headers==3.14.0
```

### Frontend (`package.json`)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.4.0"
  },
  "devDependencies": {
    "vite": "^4.3.9",
    "@vitejs/plugin-react": "^4.0.0"
  }
}
```

## 🧪 Testing

### Run Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test api
```

## 📝 Admin Interface

Access Django admin panel at: `http://localhost:8000/admin/`

Features:
- Manage grocery items
- Filter by purchase status
- Search items by name
- View creation timestamps

## 🛠️ Development Tips

### Database Migrations
```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Rollback migration
python manage.py migrate api zero
```

### Django Shell
```bash
python manage.py shell
```

### Create Sample Data
```python
from api.models import GroceryItem

GroceryItem.objects.create(
    name="Apple",
    quantity="5 pieces",
    purchased=False
)
```

## 🚀 Deployment

### Using Gunicorn
```bash
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
```

### Environment Variables
Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 📄 API Documentation

Complete API documentation using Django REST Framework browsable API is available at:
- `http://localhost:8000/api/`
- `http://localhost:8000/api/items/`

## 🤝 Contributing

Contributions are welcome! Please follow the code style and add tests for new features.

## 📄 License

MIT License

## 👤 Author

**Priyanshu Verma**

---

For questions or support, please open an issue or contact the author.
