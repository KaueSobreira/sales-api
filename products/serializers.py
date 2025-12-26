from rest_framework import serializers
from .models import Products
from brands.serializers import BrandSerializer
from categories.serializers import CategorieSerializer


class ProductSerializerBFF(serializers.ModelSerializer):
    brands = BrandSerializer()
    categorie = CategorieSerializer()

    class Meta:
        model = Products
        fields = ['id', 'name', 'brands', 'stock', 'price', 'categorie', 'is_stock']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'