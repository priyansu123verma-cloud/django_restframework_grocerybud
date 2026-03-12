# GroceryBud Development Guide

**Author:** Priyanshu Verma

## Project Setup

### 1. Backend Setup

#### Clone and Setup Virtual Environment
```bash
# Clone the repository
git clone <repository-url>
cd GroceryBud

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Configure Environment
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your settings
# Secret key generation:
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### Database Setup
```bash
# Create database tables
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser

# Create some sample data (optional)
python manage.py shell
```

#### Run Backend Server
```bash
python manage.py runserver
```
Backend runs at: `http://localhost:8000`

### 2. Frontend Setup

#### Install Dependencies
```bash
cd grocery-bud-react
npm install
```

#### Configure API URL (Optional)
Create a `.env` file in `grocery-bud-react/`:
```
REACT_APP_API_URL=http://localhost:8000/api
```

#### Run Frontend Server
```bash
npm start
```
Frontend runs at: `http://localhost:3000`

## Development Workflow

### Making Changes to Models

1. **Modify model in** `grocery/models.py`
2. **Create migration:**
   ```bash
   python manage.py makemigrations
   ```
3. **Apply migration:**
   ```bash
   python manage.py migrate
   ```

### Creating New API Endpoints

1. **Create view in** `grocery/views.py` or `core/views.py`
2. **Create serializer in** `grocery/serializers.py`
3. **Register in router in** `config/urls.py`
4. **Test endpoint using curl or Postman**

### Frontend Development

1. **Create React components in** `grocery-bud-react/src/`
2. **Update** `App.js` or create separate component files
3. **Changes auto-reload with npm start**

## Testing

### Backend Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test core
python manage.py test grocery

# Run with verbosity
python manage.py test --verbosity=2
```

### Frontend Testing (Optional)
```bash
cd grocery-bud-react
npm test
```

## Admin Interface

Access Django admin at: `http://localhost:8000/admin/`

- Username: (your superuser username)
- Password: (your superuser password)

Manage:
- Grocery items
- Users
- Permissions
- Groups

## API Documentation

### Accessing API
- All API endpoints: `http://localhost:8000/api/`
- Hello endpoint: `http://localhost:8000/api/hello/`
- Grocery items: `http://localhost:8000/api/grocery-items/`

### Using Django Rest Framework Browser
DRF provides a browsable API at each endpoint. Simply visit the URL in your browser.

### CORS Configuration
CORS is configured in `config/settings.py`. By default, `localhost:3000` is allowed. Add more origins as needed.

## Deployment Checklist

Before deploying:

1. **Security:**
   - [ ] Set DEBUG=False
   - [ ] Change SECRET_KEY
   - [ ] Update ALLOWED_HOSTS
   - [ ] Configure HTTPS

2. **Database:**
   - [ ] Use production database (PostgreSQL recommended)
   - [ ] Run migrations
   - [ ] Backup production data

3. **Static/Media Files:**
   - [ ] Collect static files
   - [ ] Configure static file serving
   - [ ] Test file uploads

4. **Frontend:**
   - [ ] Build React app: `npm run build`
   - [ ] Copy dist folder to Django templates

5. **Testing:**
   - [ ] Run full test suite
   - [ ] Test all API endpoints
   - [ ] Test frontend functionality

## Docker Deployment (Optional)

Create `Dockerfile` in project root:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t grocerybud .
docker run -p 8000:8000 grocerybud
```

## Troubleshooting

### Module Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Database Errors
```bash
# Reset database (development only!)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### CORS Errors
- Check CORS_ALLOWED_ORIGINS in config/settings.py
- Ensure frontend URL is added to ALLOWED_HOSTS

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### React Build Issues
```bash
cd grocery-bud-react
rm -rf node_modules
npm install
npm start
```

## Debugging

### Django Debug Toolbar (Optional)

Install:
```bash
pip install django-debug-toolbar
```

Add to INSTALLED_APPS in `config/settings.py`:
```python
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
```

## Performance Tips

1. **Database Optimization:**
   - Use select_related() for foreign keys
   - Use prefetch_related() for reverse relations
   - Index commonly queried fields

2. **API Optimization:**
   - Implement pagination
   - Use caching
   - Compress responses

3. **Frontend Optimization:**
   - Lazy load images
   - Code splitting
   - Minify assets

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Render Deployment](https://render.com/docs)

## Contact

**Author:** Priyanshu Verma

For questions or issues, please open a GitHub issue.
