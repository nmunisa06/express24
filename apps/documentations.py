# elasticsearch settings

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from apps.models import Product


@registry.register_document
class ProductElasticSearchDocument(Document):
    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
        }

    class Django:
        model = Product
        fields ={}