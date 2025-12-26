from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductCreateListView.as_view(), name='product-create-list'),
    path('products/<int:pk>/', views.ProductUpdateDeleteListView.as_view(), name='product-update-delete-list'),
]