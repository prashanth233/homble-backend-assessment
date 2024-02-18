from rest_framework import serializers
from .models import Product
from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """
    To show list of products.
    """

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'is_refrigerated', 'category', 'edited_at', 'ingredients'] 
