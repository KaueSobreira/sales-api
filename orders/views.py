from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Order
from .serializers import OrderCreateSerializer, OrderSerializer


class OrderCreateListView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateSerializer

class OrderUpdateDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateSerializer

    lookup_field = 'public_id'
