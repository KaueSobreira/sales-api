from django.urls import path
from . import views


urlpatterns = [
    path('paymentmethods/', views.PaymentMethodCreateListView.as_view(), name='payment-create-list-view'),
    path('paymentmethods/<int:pk>/', views.PaymentMethodUpdateDestroyListView.as_view(), name='payment-update-destroy-list-view'),
]