from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from app import serializer, models
from utils.viewsets import ModelViewSet

"""
使用django建立一个玩家分数排行榜服务，服务向客户端提供两个接口:

1. [upload]客户端上传客户端号和分数(注意：并不会上传排名,客户端无法上传排名),同一个客户端可以多次上传分数，取最新的一次分数
2. [ranking]客户端查询排行榜

可以查询任何名次段，例如可以查询排名20~30的表格
每次查询的最后，都要附加上调用接口的客户端的排名，如例子所示为客户端5的排名被附加到了最后


自己设计接口地址，参数，返回值,并实现接口
自己设计测试用例，完成接口后，自己测试,并使用git提交代码，将测试结果以及仓库地址给面试官看
"""


class UpdateViewSet(ModelViewSet):
    serializer_class = serializer.UpdateSerializer
    queryset = models.update.objects.filter()

    def create(self, request, *args, **kwargs):
        number_first = self.queryset.filter(key__uid=request.data.get('uid')).first()

        if not number_first:
            key = models.customer(uid=request.data.get('uid'))
            key.save()
        else:
            key = number_first.key

        data = request.data
        data['key'] = key.pk
        serializers = self.get_serializer(data=data)
        serializers.is_valid(raise_exception=True)
        self.perform_create(serializers)

        headers = self.get_success_headers(serializers.data)
        return Response(serializers.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        no_page = self.request.query_params.get('no_page', None)

        if no_page:
            """
            该字段用来判断是否经过分页处理
            """
            serializers = self.get_serializer_list(queryset, many=True)
            return Response(serializers.data)
        else:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializers = self.get_serializer_list(page, many=True)
                return self.get_paginated_response(serializers.data)

            serializers = self.get_serializer_list(queryset, many=True)
            return Response(serializers.data)


class rankingViewSet(ModelViewSet):
    serializer_class = serializer.RankingSerializer
    queryset = models.ranking.objects.filter()

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        no_page = self.request.query_params.get('no_page', None)
        uid = self.request.query_params.get('uid', None)
        uid_date = {}
        if uid:
            serializers = self.get_serializer_list(queryset.filter(key__uid=uid).first())
            return Response(serializers.data)

        print('xxx')
        if no_page:
            """
            该字段用来判断是否经过分页处理
            """
            print('no_page')
            serializers = self.get_serializer_list(queryset, many=True)
            return Response(serializers.data)
        else:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializers = self.get_serializer_list(page, many=True)
                return self.get_paginated_response(serializers.data)

            serializers = self.get_serializer_list(queryset, many=True)
            return Response(serializers.data)
