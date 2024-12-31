from itertools import product

from django.urls import path
from apps.views.viewsAdmin import ProductCreateAPIView, ProductEditAPIView, CategoryCreateAPIView, CategoryEditAPIView, \
    OrderProductCreateAPIView
from apps.views.viewsCourier import OrderProductEditAPIView

urlpatterns = [
    path('order/', OrderProductCreateAPIView.as_view(), name='order_product'),
    path('product-edit/', OrderProductEditAPIView.as_view(), name='order_product_edit'),
    path('product/', ProductCreateAPIView.as_view(), name='product_list'),
    path('product-edit/', ProductEditAPIView.as_view(), name='product_edit'),
    path('category-list/', CategoryCreateAPIView.as_view(), name='category_list'),
    path('category-edit/', CategoryEditAPIView.as_view(), name='category_edit'),

]
