from django.db import models


class Address(models.Model):
    zip_code = models.IntegerField()
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='address'
    )
