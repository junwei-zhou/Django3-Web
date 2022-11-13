from rest_framework import serializers
from .models import PersonInfo, Vocation

# 定义Serializer类
# 设置模型Vocation的字段name的下拉内容
nameList = PersonInfo.objects.values('name').all()
NAME_CHOICES = [item['name'] for item in nameList]
class MySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    job = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    payment = serializers.CharField(max_length=100)
    # name = serializers.ChoiceField(choices=NAME_CHOICES, default=1)
    # 模型Vocation的字段name是外键字段，它指向模型PersonInfo
    # 因此外键字段可以使用PrimaryKeyRelatedField
    name = serializers.PrimaryKeyRelatedField(queryset=nameList)

    # 重写create函数，将API数据保存到数据表index_vocation
    def create(self, validated_data):
        return Vocation.objects.create(**validated_data)

    # 重写update函数，将API数据更新到数据表index_vocation
    def update(self, instance, validated_data):
        return instance.update(**validated_data)