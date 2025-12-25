from rest_framework import generics
from .models import Brands
from .serializers import BrandSerializer


class BrandCreateListView(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brands.objects.all()

class BrandUpdateDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brands.objects.all()