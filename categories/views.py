from rest_framework import generics
from .models import Categorie
from .serializers import CategorieSerializer


class CategorieCreateListView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieUpdateDeleteListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer