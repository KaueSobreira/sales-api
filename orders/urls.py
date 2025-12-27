from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderCreateListView.as_view(), name='order-create-list-view'),
    path('orders/<int:pk>/', views.OrderUpdateDestroyListView.as_view(), name='order-update-destroy-list-view'),
]