from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer


class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateDeleteListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer