from rest_framework import serializers
from .models import Category,Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name')
    
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('id','title','category','cost','image','desc')