from django.db import models
from categories.models import Categorie
from brands.models import Brands


class Products(models.Model):
    name = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)
    brands = models.ForeignKey(Brands, on_delete=models.PROTECT)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    is_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
