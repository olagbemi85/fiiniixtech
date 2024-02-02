from rest_framework import serializers

from .models import *



class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields= ['name', 'slug']

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields= '__all__'