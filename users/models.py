from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=70, unique=True)
    password = models.CharField(max_length=120)
    contact = models.CharField(max_length=20)
    full_name = models.CharField(max_length=120)
    is_seller = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"<User ({self.id})-({self.full_name})>"
