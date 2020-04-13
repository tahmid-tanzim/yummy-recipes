# Yummy Recipes
A recipe catalog API developed with Django REST Framework, PostgreSQL, Docker  

### Docker Compose Build
docker-compose build

### Docker Compose UP
docker-compose up

### Create Django Project
docker-compose run api sh -c "django-admin startproject app ."

### Create Django Core App
docker-compose run api sh -c "python manage.py startapp core"

### Django Test
docker-compose run api sh -c "python manage.py test && flake8"

### Django Core App Migrations
docker-compose run api sh -c "python manage.py makemigrations core"

### Django Create SuperUser
docker-compose run api sh -c "python manage.py createsuperuser"

### Create Django User App
docker-compose run --rm api sh -c "python manage.py startapp user"