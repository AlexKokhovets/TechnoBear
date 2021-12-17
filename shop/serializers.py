from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'image',
            'description',
            'price',
            'created',
            'updated',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
        ]
