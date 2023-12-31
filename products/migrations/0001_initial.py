# Generated by Django 4.2.2 on 2023-07-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("roupas", "Roupas"),
                            ("calçados", "Calcados"),
                            ("acessorios", "Acessorios"),
                        ],
                        max_length=20,
                    ),
                ),
                ("price", models.FloatField()),
                ("stock_quantity", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image_url", models.URLField(default=None, null=True)),
            ],
        ),
    ]
