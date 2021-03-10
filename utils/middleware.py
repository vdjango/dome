# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status


class WuhePermissionMiddleware(MiddlewareMixin):

    def process_request(self, request, *args):
        # print(request.META)
        key = request.META.get("HTTP_KEY")
        if not isinstance(key, str):
            key = str(key)
        if key != "wuhe":
            return HttpResponse({"error": "请求被拒绝"}, status=status.HTTP_401_UNAUTHORIZED)
        return
