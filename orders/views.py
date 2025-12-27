from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Order
from .serializers import OrderCreateSerializer


class OrderCreateListView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

class OrderUpdateDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    lookup_field = 'public_id'
