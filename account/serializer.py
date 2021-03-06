'''

Copyright (C) 2019 张珏敏.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from . import models


class UserBaseSerializer(serializers.ModelSerializer):
    '''
    用户信息序列化
    '''

    def create(self, validated_data):
        instance = super(UserBaseSerializer, self).create(validated_data)
        models.Integral(key=instance).save()
        return instance

    class Meta:
        model = models.User
        exclude = ['password']


"""
Start Auth
"""


class RegisterSerializer(UserBaseSerializer):
    '''
    用户注册序列化
    API： authorization-register
    '''

    class Meta:
        model = UserBaseSerializer.Meta.model
        fields = ['id', 'email', 'first_name', 'password']
        pass


"""
End Auth
"""



class UserSerializer(UserBaseSerializer, WritableNestedModelSerializer):
    '''
    用户序列化
    '''

    def create(self, validated_data):
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(UserSerializer, self).update(instance, validated_data)

    pass
