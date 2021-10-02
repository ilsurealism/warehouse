from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    gross_cost = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('code', 'price', 'gross_cost')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code', 'category', 'manufacturer', 'quantity', 'price')
