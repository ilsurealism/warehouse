from rest_framework import serializers
from .models import Product, Category, Manufacturer


class ProductSerializer(serializers.ModelSerializer):
    gross_cost = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('code', 'price', 'gross_cost')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code', 'category', 'manufacturer', 'quantity', 'price')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name',)

