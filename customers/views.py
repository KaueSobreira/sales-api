from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import ClientSerializer
from .models import Client


class ClientCreateListView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer