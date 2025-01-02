from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models.products import Cart, CartItem
from apps.serializers import CartModelSerializer, CartItemModelSerializer

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