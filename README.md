# 排行榜服务

> 使用django建立一个玩家分数排行榜服务
> 包含分页，Jwt认证等

1. `[upload]` 上传客户端号和分数(客户端无法上传排名),同一个客户端可以多次上传分数，取最新的一次分数
2. `[ranking]`客户端查询排行榜
3. 单元测试用例 `python manage.py test`

## 例子说明

* 可以查询任何名次段，例如可以查询排名20~30的表格
* 每次查询的最后，都要附加上调用接口的客户端的排名，如例子所示为客户端5的排名被附加到了最后

## 任务说明

1. 自己设计接口地址，参数，返回值,并实现接口
2. 自己设计测试用例，完成接口后，自己测试

## 测试

> [POST] http://127.0.0.1:8000/app/update/
> 添加客户端分数（相同客户端编号 添加多个分数 排名保留最高分数）

```json
{
    "uid": 2, // 客户端编号
    "number": 90 //客户端分数
}
```

> [GET] http://127.0.0.1:8000/app/ranking/?uid=5 [未完成]
> 查询客户端5的排名

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json ;utf-8
Vary: Accept

{
    "id": 8,
    "uid": 5, // 客户端编号
    "number": 1697, //客户端分数
    "key": 8
}
```

> [GET] http://127.0.0.1:8000/app/ranking/
> 查询所以客户端5的排名
> 相同客户端编号 添加多个分数 排名保留最高分数

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json ;utf-8
Vary: Accept

{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "uid": 2,
            "number": 9110,
            "key": 4
        },
        {
            "id": 13,
            "uid": 10,
            "number": 7697,
            "key": 13
        },
        {
            "id": 11,
            "uid": 8,
            "number": 6697,
            "key": 11
        },
        {
            "id": 12,
            "uid": 9,
            "number": 4697,
            "key": 12
        },
        {
            "id": 10,
            "uid": 7,
            "number": 1997,
            "key": 10
        }
        ...
    ]
}
```

## 关于接口分页部分说明

> 为了展示相关，默认展示3条数据
> 如果需要查看指定数目数据，请通过偏移量进行调整

* offset 偏移量
* limit 展示数据条目

[GET] /?limit=3&offset=3

> 查询排名3~8的数据
> offset 偏移量设置3，limit 数据条目设置 8-3=5

[GET] http://127.0.0.1:8000/app/ranking/?limit=5&offset=3

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json ;utf-8
Vary: Accept

{
    "count": 10,
    "next": "http://127.0.0.1:8000/app/ranking/?limit=5&offset=8",
    "previous": "http://127.0.0.1:8000/app/ranking/?limit=5",
    "results": [
        {
            "id": 12,
            "uid": 9,
            "number": 4697,
            "key": 12
        },
        {
            "id": 10,
            "uid": 7,
            "number": 1997,
            "key": 10
        },
        {
            "id": 7,
            "uid": 4,
            "number": 1956,
            "key": 7
        },
        {
            "id": 8,
            "uid": 5,
            "number": 1697,
            "key": 8
        },
        {
            "id": 9,
            "uid": 6,
            "number": 1606,
            "key": 9
        }
    ]
}

```
