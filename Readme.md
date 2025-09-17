### Django Portafolio, Ejemplo Práctico

https://www.youtube.com/watch?v=zBjMF6je24U&t=6091s

Entorno virtual
```
python -m venv venv
venv\Scripts\activate
```

Ejecutar entorno virtual
```
venv\Scripts\activate
```

Instalar Django
```
pip install django    
```

Instalar Django admin
```
django-admin startproject django_portfolio .
```

Ejecutar Server
```
python manage.py runserver
```

Creación de Apps
```
python manage.py startapp blog
python manage.py startapp portfolio
```

Migraciones
```
python manage.py makemigrations
python manage.py migrate
```

Panel Admin
```
python manage.py createsuperuser
```

Requirements
```
pip freeze > requirements.txt
```