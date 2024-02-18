from rest_framework import serializers
from categories.models import Category
from products.serializers import ProductListSerializer

class CategorySerializer(serializers.ModelSerializer):
    count_products = serializers.IntegerField()
    products = ProductListSerializer(many = True, read_only = True)

    class Meta:
        model = Category
        fields = '__all__'