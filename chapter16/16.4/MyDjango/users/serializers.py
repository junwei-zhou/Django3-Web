from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
# 定义ModelSerializer类
class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(label='用户凭证', read_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'token')

    def create(self, validated_data):
        # 在Serializer类中重写create方法
        user = super().create(validated_data=validated_data)
        # 密码加密
        user.set_password(validated_data['password'])
        user.save()
        # 根据用户创建token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        # 在用户对象user添加token属性
        user.token = token
        return user