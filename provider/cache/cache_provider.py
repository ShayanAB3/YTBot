class CacheProvider:
    drivers = {
        "file":{
            "type":"json",
            "dirname":"cache"
        },
        "redis": {
            "host":"",
            "user":"",
        }
    }