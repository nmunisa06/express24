from rest_framework.serializers import ModelSerializer

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
        fields = '__all__'


class CartItemModelSerializer(ModelSerializer):
    products = ProductModelSerializer(many=True)

    class Meta:
        model = CartItem
        fields = '__all__'
