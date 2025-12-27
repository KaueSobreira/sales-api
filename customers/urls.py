from django.urls import path
from . import views


urlpatterns = [
    path('clients/', views.ClientCreateListView.as_view(), name='client-create-list-view'),
    path('clients/<int:pk>', views.ClientUpdateDestroyListView.as_view(), name='client-update-destroy-list-view'),
]