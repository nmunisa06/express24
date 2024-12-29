from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView


@extend_schema(tags=['products'])
class ProductsAPIView(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        ...

