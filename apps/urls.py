from django.urls import path
from apps.views.viewsAdmin import (
    AdminCartItemCreateAPIView, AdminCartItemEditAPIView,
    AdminProductCreateAPIView, AdminProductEditAPIView,
    AdminCategoryCreateAPIView, AdminCategoryEditAPIView)

from apps.views.viewsCourier import CourierCartEditAPIView, CourierCartItemEditAPIView

urlpatterns = [
    # Admin views
    path('admin/product-create/', AdminProductCreateAPIView.as_view(), name='admin-product-list-create'),
    path('admin/product-edit/<int:pk>/', AdminProductEditAPIView.as_view(), name='admin-product-edit'),

    path('admin/category-create/', AdminCategoryCreateAPIView.as_view(), name='admin-category-list-create'),
    path('admin/category-edit/<int:pk>/', AdminCategoryEditAPIView.as_view(), name='admin-category-edit'),

    path('admin/cart-item-create/', AdminCartItemCreateAPIView.as_view(), name='admin-cart-create'),
    path('admin/cart-items-edit/<int:pk>/', AdminCartItemEditAPIView.as_view(), name='admin-cart-items-edit'),


    # Courier views
    path('courier/cart-edit/<int:pk>/', CourierCartEditAPIView.as_view(), name='courier-cart-edit'),
    path('courier/cart-items-edit/<int:pk>/', CourierCartItemEditAPIView.as_view(), name='courier-cart-item-edit'),

]

