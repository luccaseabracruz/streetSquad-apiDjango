from django.db import models


class Status_Choices(models.TextChoices):
    REALIZADO = "realizado"
    EM_ANDAMENTO = "em andamento"
    CONCLUIDO = "concluido"


class Request(models.Model):
    status = models.CharField(
        max_length=20,
        choices=Status_Choices.choices,
        default=Status_Choices.REALIZADO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ManyToManyField(
        "products.Product",
        related_name="requests",
        through='RequestProducts'
    )
    """ alterar product(s) """

    buyer = models.ForeignKey(
        "users.User",
        related_name="requests",
        on_delete=models.CASCADE
    )

    seller = models.IntegerField(default=None, null=True)


class RequestProducts(models.Model):
    request = models.ForeignKey("requests.Request", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)
    seller = models.IntegerField(default=None, null=True)
