from django.db import models


class CategoryChoices(models.TextChoices):
    ROUPAS = "roupas"
    CALCADOS = "calçados"
    ACESSORIOS = "acessorios"


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models .CharField(
        max_length=20,
        choices=CategoryChoices.choices
    )
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products"
    )
    image_url = models.URLField(null=True, default='https://uploaddeimagens.com.br/imagens/zrwGMsE')

    def __repr__(self) -> str:
        return f"<Product ({self.id})-({self.name})>"
