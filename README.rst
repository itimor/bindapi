# bind dlz dns api

# 设置token

```
curl -X POST -d "username=admin&password=password123" http://localhost:8000/api/api-token-auth/

{
    "token": "ad0fd6577b32e0ca4a12bacd30e0155925a64a3b"
}
```

# 携带token获取records

```
curl -H "Authorization: token ad0fd6577b32e0ca4a12bacd30e0155925a64a3b" http://localhost:8000/api/records/

[
    {
        "url": "http://127.0.0.1:8888/api/records/4/",
        "id": 4,
        "zone": "oo.com",
        "name": "www",
        "type": "A",
        "value": "1.1.1.22",
        "ttl": 600,
        "mx_priority": null,
        "serial": null,
        "refresh": null,
        "retry": null,
        "expire": null,
        "minimum": null,
        "resp_person": "",
        "primary_ns": "",
        "create_time": "2018-04-14T19:29:10",
        "update_time": "2018-04-14T19:29:34.311111"
    },
    {
        "url": "http://127.0.0.1:8888/api/records/5/",
        "id": 5,
        "zone": "oo.com",
        "name": "bbs",
        "type": "CNAME",
        "value": "www",
        "ttl": 600,
        "mx_priority": null,
        "serial": null,
        "refresh": null,
        "retry": null,
        "expire": null,
        "minimum": null,
        "resp_person": null,
        "primary_ns": null,
        "create_time": "2018-04-14T19:29:13",
        "update_time": "2018-04-14T19:29:21"
    }
]
```