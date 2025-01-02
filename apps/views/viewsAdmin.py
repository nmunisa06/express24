from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.models.products import Product, Category, Cart, CartItem
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, CartModelSerializer, CartItemModelSerializer



@extend_schema(tags=['product-create'])
class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAdminUser]
    filter_backends = filters.DjangoFilterBackend
    filterset_fields = 'category', 'price',


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


@extend_schema(tags=['cart'])
class CartCreateAPIView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['cart'])
class CartEditAPIView(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['in-cart-products'])
class CartItemCreateAPIView(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemModelSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['in-cart-products'])
class CartItemEditAPIView(RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemModelSerializer
    permission_classes = [IsAuthenticated]






