from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.documentations import ProductElasticSearchDocument
from apps.models.products import Category, Product, Cart, CartItem
from apps.models.users import User


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CartModelSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = 'id', 'user_id', 'products',

    def validate(self, data):
        house_numb = data.get('house_numb')
        apartment_numb = data.get('apartment_numb')

        if not house_numb and not apartment_numb:
            raise ValidationError("Either house number or apartment number must be provided.")
        return data


class CartItemModelSerializer(ModelSerializer):
    products = ProductModelSerializer(many=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CourierCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'status', 'products', 'updated_at', 'courier']


class ProductElasticSearchDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductElasticSearchDocument

        fields = (
            'id',
            'name',
            'description',
        )

