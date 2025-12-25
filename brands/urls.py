from django.urls import path
from . import views


urlpatterns = [
    path('brands/', views.BrandCreateListView.as_view(), name='brand-list-create'),

    path('brands/<int:pk>/', views.BrandUpdateDestroyListView.as_view(), name='brand-list-update-delete'),
]