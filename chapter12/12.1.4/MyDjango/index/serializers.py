from rest_framework import serializers
from .models import Vocation, PersonInfo


# 定义ModelSerializer类
class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = '__all__'


# 定义ModelSerializer类
class VocationSerializer(serializers.ModelSerializer):
    name = PersonInfoSerializer()
    class Meta:
        model = Vocation
        fields = ('id', 'job', 'title', 'payment', 'name')

    def create(self, validated_data):
        # 从validated_data获取模型PersonInfo的数据
        name = validated_data.get('name', '')
        id = name.get('id', 0)
        p = PersonInfo.objects.filter(id=id).first()
        # 根据id判断模型PersonInfo是否存在数据对象
        # 若存在数据对象，只对Vocation新增数据
        # 若不存在，首先对模型PersonInfo新增数据
        # 然后再对模型Vocation新增数据
        if not p:
            p = PersonInfo.objects.create(**name)
        data = validated_data
        data['name'] = p
        v = Vocation.objects.create(**data)
        return v

    def update(self, instance, validated_data):
        # 从validated_data获取模型PersonInfo的数据
        name = validated_data.get('name', '')
        id = name.get('id', 0)
        p = PersonInfo.objects.filter(id=id).first()
        # 判断外键name是否存在模型PersonInfo
        if p:
            # 若存在，首先更新模型PersonInfo的数据
            PersonInfo.objects.filter(id=id).update(**name)
            # 然后更新模型Vocation的数据
            data = validated_data
            data['name'] = p
            id = validated_data.get('id', '')
            v = Vocation.objects.filter(id=id).update(**data)
            return v