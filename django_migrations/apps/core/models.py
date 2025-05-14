from django.db import models


class Product(models.Model):
    name = models.CharField(
        default="",
        max_length=200
    )

    sku = models.CharField(
        default="",
        max_length=30
    )
