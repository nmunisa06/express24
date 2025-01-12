from django_filters import RangeFilter, CharFilter
from django_filters.rest_framework import FilterSet, NumberFilter

from apps.models import Product


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='iexact')

    price = NumberFilter()
    min_price = NumberFilter(name="price", lookup_expr='gte')
    max_price = NumberFilter(name="price", lookup_expr='lte')

    # price = RangeFilter()

    class Meta:
        model = Product
        fields = ['category']
