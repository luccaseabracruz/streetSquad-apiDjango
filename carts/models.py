from django.db import models


# Create your models here.
class Cart(models.Model):
    user = models.ManyToManyField(
        "users.User",
        related_name="user"
    )
    product = models.ManyToManyField(
        "products.Product",
        related_name="product"
    )
