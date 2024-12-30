from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.models.products import Product
from apps.serializers import ProductModelSerializer


@extend_schema(tags=['products'])
class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


