from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.views import ProductCreateAPIView


urlpatterns = [
    path('product/', ProductCreateAPIView.as_view(), name='product_list'),
]
