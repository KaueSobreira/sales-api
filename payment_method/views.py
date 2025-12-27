from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer


class PaymentMethodCreateListView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class PaymentMethodUpdateDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
