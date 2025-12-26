from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategorieCreateListView.as_view(), name='categorie-create-list'),
    path('categories/<int:pk>', views.CategorieUpdateDeleteListView.as_view(), name='categorie-list-update-delete'),
]