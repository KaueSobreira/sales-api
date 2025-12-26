from django.db import models
from categories.models import Categorie
from brands.models import Brands


class Products(models.Model):
    name = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)
    brands = models.ForeignKey(Brands, on_delete=models.PROTECT)
    stock = models.IntegerField()
    price = models.DecimalField()

    def __str__(self):
        return self.name