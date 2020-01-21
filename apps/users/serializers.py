#!/user/bin/evn Python3 
# -*- coding:utf-8 -*-
# project:PyCharm
# serializers.py
# 序列化器校验
# author:ZhaoHeXin
# creation 2020/1/21--14:52

from rest_framework import serializers
from .models import User
from .models import Directory
from .models import Menu
from .models import Button
from .models import UserRole


class UserModelSerializers(serializers.ModelSerializer):
    """
    用户名/注册序列化器
    """

    class Meta:
        model = User
        fields = "__all__"


class DirectoryModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = Directory
        fields = "__all__"


class MenuModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = Menu
        fields = "__all__"


class ButtonModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = Button
        fields = "__all__"


class UserRoleModelSerializers(serializers.ModelSerializer):
    """
    目录配置表序列化器
    """

    class Meta:
        model = UserRole
        fields = "__all__"
