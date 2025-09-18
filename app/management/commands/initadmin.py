# app/management/commands/initadmin.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Create default superuser if not exists"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f"Superuser {username} created"))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser {username} already exists"))
