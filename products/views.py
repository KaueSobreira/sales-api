from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer, ProductSerializerBFF


class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializerBFF
        return ProductSerializer


class ProductUpdateDeleteListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializerBFF
        return ProductSerializer