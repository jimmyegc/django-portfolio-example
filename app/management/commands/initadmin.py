from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Crea un superusuario automáticamente o actualiza la contraseña si ya existe'

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

        user, created = User.objects.get_or_create(username=username)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)  # asegúrate de actualizar la contraseña
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Superusuario '{username}' creado correctamente"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superusuario '{username}' actualizado correctamente"))
