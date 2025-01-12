from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.models.products import Cart
from apps.permissions import IsCourier
from apps.serializers import CartModelSerializer, CourierCartSerializer


@extend_schema(tags=['customer-order'])
class CustomerOrderAPIView(ListCreateAPIView):
    queryset = Cart.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CartModelSerializer


@extend_schema(tags=['customer-order-edit'])
class CartEditAPIView(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['courier-orders'])
class CourierOrderAPIView(ListAPIView):
    queryset = Cart.objects.filter(status='pending')
    permission_classes = [IsCourier]

@extend_schema(tags=['courier-orders-update'])
class CourierOrderUpdateView(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CourierCartSerializer
    permission_classes = [IsCourier]