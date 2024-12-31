from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models.products import OrderProduct
from apps.serializers import OrderProductModelSerializer

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