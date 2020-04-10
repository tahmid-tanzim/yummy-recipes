# Yummy Recipes
A recipe catalog API developed with Django REST Framework, PostgreSQL, Docker  

### Docker Compose Build
docker-compose build

### Create Django Project
docker-compose run api sh -c "django-admin startproject app ."

### Create Django App
docker-compose run api sh -c "python manage.py startapp core"

### Django Test
docker-compose run api sh -c "python manage.py test && flake8"

### Django Migrations
docker-compose run api sh -c "python manage.py makemigrations core"
