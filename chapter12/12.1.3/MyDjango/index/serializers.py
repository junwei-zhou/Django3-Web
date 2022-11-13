from rest_framework import serializers
from .models import Vocation

# 定义ModelSerializer类
class VocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocation
        fields = '__all__'
        # fields = ('id', 'job', 'title', 'payment', 'name')