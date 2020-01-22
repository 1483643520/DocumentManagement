#!/user/bin/evn Python3
# -*- coding:utf-8 -*-
# project:PyCharm
# serializers.py
# 序列化器校验
# author:ZhaoHeXin
# creation 2020/1/21--14:52

from rest_framework.fields import CharField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.utils import api_settings
from .models import UserModel
from .models import DirectoryModel
from .models import MenuModel
from .models import ButtonModel
from .models import UserRoleModel


class UserModelSerializers(serializers.ModelSerializer):
    """
    用户名/注册序列化器
    """
    password_confirm = CharField(label="确认密码", help_text="确认密码", max_length=128, write_only=True)
    token = CharField(label="token", help_text="token", max_length=128, read_only=True)

    class Meta:
        model = UserModel
        exclude = ("groups", "user_permissions", "first_name", "last_name")
        write_only = ["password"]

        # 做一些字段数据校验
        extra_kwargs = {
            "user_name": {
                "label": "用户名",
                "help_text": "用户名",
                "min_length": 6,
                "max_length": 20,
                "error_messages": {
                    "min_length": "仅允许输入6-20个字符",
                    "max_length": "仅允许输入6-20个字符",
                }

            },
            "email": {
                "label": "邮箱",
                "help_text": "邮箱",
                "write_only": True,
                "required": True,
                "validators": [UniqueValidator(queryset=UserModel.objects.all(), message="此邮箱已被注册")]
            },
            "password": {
                "label": "密码",
                "help_text": "密码",
                "min_length": 6,
                "max_length": 20,
                "write_only": True,
                "error_messages": {
                    "min_length": "仅允许输入6-20个字符",
                    "max_length": "仅允许输入6-20个字符",
                }
            },
        }

    def validate(self, attrs):
        """
        密码与确认密码校验
        :param attrs:
        :return:
        """
        password_ = attrs["password_confirm"]
        if attrs["password"] != password_:
            raise serializers.ValidationError("密码与确认密码必须一致")
        del attrs["password_confirm"]
        return attrs

    def create(self, validated_data):
        print(validated_data)
        # 重置加密密码
        # create_user会对密码进行加密
        if validated_data["is_staff"]:
            user = UserModel.objects.create_superuser(**validated_data)
        else:
            user = UserModel.objects.create_user(**validated_data)
        # 生成token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user


class DirectoryModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = DirectoryModel
        fields = "__all__"


class MenuModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = MenuModel
        fields = "__all__"


class ButtonModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = ButtonModel
        fields = "__all__"


class UserRoleModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = UserRoleModel
        fields = "__all__"
