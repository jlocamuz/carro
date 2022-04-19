from rest_framework import fields, serializers
from .models import Product, Distributor


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'
    
class DistributorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Distributor
        fields = '__all__'