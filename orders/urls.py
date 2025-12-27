from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderCreateListView.as_view(), name='order-create-list-view'),
    path('orders/<uuid:public_id>/', views.OrderUpdateDestroyListView.as_view(), name='order-update-destroy-list-view'),
]