# Generated by Django 4.2.2 on 2023-07-05 17:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("requests", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="request",
            name="products",
        ),
    ]
