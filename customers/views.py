from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import ClientSerializer, ClientSerializerBFF
from .models import Client


class ClientCreateListView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientSerializerBFF
        return ClientSerializer

class ClientUpdateDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Client.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientSerializerBFF
        return ClientSerializer