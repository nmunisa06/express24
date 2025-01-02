from itertools import product

from django.urls import path
from apps.views.viewsAdmin import ProductCreateAPIView, ProductEditAPIView, CategoryCreateAPIView, CategoryEditAPIView
from apps.views.viewsCourier import CartEditAPIView, CartCreateAPIView, CartItemCreateAPIView, CartItemEditAPIView

urlpatterns = [
    path('cartItems/', CartItemCreateAPIView.as_view(), name='in-cart-items'),
    path('cartItems-edit/', CartItemEditAPIView.as_view(), name='in-cart_items_edit'),
    path('cart/', CartCreateAPIView.as_view(), name='cart_system'),
    path('cart-edit/', CartEditAPIView.as_view(), name='cart_system_edit'),
    path('product/', ProductCreateAPIView.as_view(), name='product_list'),
    path('product-edit/', ProductEditAPIView.as_view(), name='product_edit'),
    path('category-list/', CategoryCreateAPIView.as_view(), name='category_list'),
    path('category-edit/', CategoryEditAPIView.as_view(), name='category_edit'),

]
