from typing import Any, Optional
from users.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "create admin user"

    def handle(self, *args: Any, **options: Any) -> str | None:
        admin_data = {
            "username": "admin",
            "email": "admin@mail.com",
            "password": "1234"
        }

        User.objects.create_superuser(**admin_data)
