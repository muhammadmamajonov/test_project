from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'image']

    def to_representation(self, instance):
        represented = super().to_representation(instance)
        represented['category'] = {
            'id': instance.category.id, 
            'title': instance.category.title
        }
        return represented
