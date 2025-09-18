# app/management/commands/initadmin.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Crea un superusuario automáticamente si no existe'

    def handle(self, *args, **options):
        # Tomamos las credenciales desde variables de entorno
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

        # Verificamos si ya existe el superusuario
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"Superusuario '{username}' ya existe"))
        else:
            # Creamos el superusuario
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superusuario '{username}' creado correctamente"))
