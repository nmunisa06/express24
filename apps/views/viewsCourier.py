from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateAPIView

from apps.models.products import Cart, CartItem
from apps.permissions import IsCourier
from apps.serializers import CartModelSerializer, CartItemModelSerializer

@extend_schema(tags=['cart'])
class CourierCartEditAPIView(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = [IsCourier]

@extend_schema(tags=['cart-item-edit'])
class CourierCartItemEditAPIView(RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemModelSerializer
    permission_classes = [IsCourier]