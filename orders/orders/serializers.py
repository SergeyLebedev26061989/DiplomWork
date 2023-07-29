from rest_framework import serializers


from orders.models import User, Category, Product, ProductInfo, Parameter, Order, OrderItem, ProductParameter, Contact


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'shop', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name']

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['product', 'shop', 'quantity', 'price', 'price_rrc']

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['name']

class ProductParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ['product_info', 'parameter', 'value']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'dt', 'status']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'shop', 'quantity']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'phone']

class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts']
        read_only_fields = ('id', 'first_name')
