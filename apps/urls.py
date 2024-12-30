from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.views import ProductCreateAPIView, ProductEditAPIView, CategoryCreateAPIView, CategoryEditAPIView

urlpatterns = [
    path('product/', ProductCreateAPIView.as_view(), name='product_list'),
    path('product-edit/', ProductEditAPIView.as_view(), name='product_edit'),
    path('category-list/', CategoryCreateAPIView.as_view(), name='category_list'),
    path('category-edit/', CategoryEditAPIView.as_view(), name='category_edit'),

]
