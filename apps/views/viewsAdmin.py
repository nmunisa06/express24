
from django_filters import rest_framework
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     RetrieveUpdateAPIView, CreateAPIView, ListAPIView)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.filters import ProductFilter
from apps.models.products import Product, Category, CartItem
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, CartItemModelSerializer


@extend_schema(tags=['product-create'])
class AdminProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter



@extend_schema(tags=['product-edit'])
class AdminProductEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=['category-create'])
class AdminCategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['category-edit'])
class AdminCategoryEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['cart-item-create'])
class AdminCartItemCreateAPIView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemModelSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['cart-item-edit'])
class AdminCartItemEditAPIView(RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemModelSerializer
    permission_classes = [IsAdminUser]


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You have access!"})




