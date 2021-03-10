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

from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from . import models


class CustomerSerializer(serializers.ModelSerializer):
    """同一个客户端可以多次上传分数"""
    class Meta:
        model = models.customer
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    """同一个客户端可以多次上传分数"""
    uid = serializers.SerializerMethodField()

    def get_uid(self, ins):
        return ins.key.uid

    class Meta:
        model = models.update
        fields = '__all__'


"""客户端上传分数"""




class RankingSerializer(WritableNestedModelSerializer):
    """客户端上传分数"""
    key = CustomerSerializer(many=True)

    class Meta:
        model = models.update
        fields = '__all__'
