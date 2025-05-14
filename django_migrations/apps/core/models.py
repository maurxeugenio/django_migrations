from django.db import models
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(
        default="",
        max_length=200
    )
    sku = models.CharField(
        default="",
        max_length=30
    )
    price = models.DecimalField(
        default=Decimal("0.00"),
        decimal_places=2,
        max_digits=20
    )
    description = models.CharField(
        max_length=400,
        default=""
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
  