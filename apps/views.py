from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.models.products import Product, Category
from apps.serializers import ProductModelSerializer, CategoryModelSerializer


@extend_schema(tags=['products'])
class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

@extend_schema(tags=['products-edit'])
class ProductEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

@extend_schema(tags=['category'])
class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

@extend_schema(tags=['category-edit'])
class CategoryEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer