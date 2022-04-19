from rest_framework import serializers

from .models import *

# Serializers allow complex data such as querysets and model instances to be converted 
# to native Python datatypes that can then be easily rendered into JSON, XML or other content types. 
# probando rama julia

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ClientDetail
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sale
        fields = '__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ShoppingCart
        fields = '__all__'

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SaleDetail
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CartDetail
        fields = '__all__'