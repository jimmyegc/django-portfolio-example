

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crea un superusuario por defecto si no existe'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = 'admin'      # Cambia esto si quieres otro usuario
        email = 'admin@example.com'
        password = 'admin123'   # Cambia la contraseña por algo seguro

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado correctamente.'))
        else:
            self.stdout.write(self.style.WARNING(f'Superusuario "{username}" ya existe.'))


