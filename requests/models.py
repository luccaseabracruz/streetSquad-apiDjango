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
    product_quantily = models.IntegerField()

    product = models.ForeignKey(
        "products.Product",
        related_name="requests",
        on_delete=models.CASCADE
    )

    buyer = models.ForeignKey(
        "users.User",
        related_name="requests",
        on_delete=models.CASCADE
    )
