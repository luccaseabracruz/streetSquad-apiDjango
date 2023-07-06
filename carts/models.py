from django.db import models


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user"
    )
    product = models.ManyToManyField(
        "products.Product",
        related_name="products",
        through="CartProducts"
    )


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)
