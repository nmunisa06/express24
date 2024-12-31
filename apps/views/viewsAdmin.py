from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.models.products import Product, Category, OrderProduct
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, OrderProductModelSerializer


@extend_schema(tags=['product-create'])
class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['products-edit'])
class ProductEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=['category-create'])
class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['category-edit'])
class CategoryEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=['product-order'])
class OrderProductCreateAPIView(ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductModelSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['product-order'])
class OrderProductEditAPIView(RetrieveUpdateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductModelSerializer
    permission_classes = [IsAuthenticated]






