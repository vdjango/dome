from rest_framework import status
from rest_framework.response import Response


def verify_key(request):
    print(request.META)
    key = request.META.get("HTTP_KEY")
    if not isinstance(key, str):
        key = str(key)
    if key != "wuhe":
        return 1, Response({"error": "请求被拒绝"}, status=status.HTTP_400_BAD_REQUEST)
    return 0, key