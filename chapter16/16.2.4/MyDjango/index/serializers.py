from rest_framework import serializers
from .models import Product


# 定义ModelSerializer类
class ProductSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = Product
        fields = ('username', 'name', 'type')
