from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('docs.urls')),

    path('api/v1/', include('brands.urls')),

    path('api/v1/', include('categories.urls')),
]
