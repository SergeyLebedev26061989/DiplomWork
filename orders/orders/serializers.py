from rest_framework import serializers

from models import Shop, Category, Product, ProductInfo, Parameter, Order, OrderItem, ProductParameter, Contact


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'url']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'shop', 'name']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name']

class ProductInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['product', 'shop', 'name', 'quantity', 'price', 'price_rrc']

class ParameterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['name']

class ProductParameterSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ['product_info', 'parameter', 'value']

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'dt', 'status']

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'shop', 'quantity']

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'phone']

class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts']
        read_only_fields = ('id',)
