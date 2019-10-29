import redis

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379

rdb = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
# 往redis数据库插入数据
rdb.set("key", "value")
# 从redis数据库获取数据
print(rdb.get("key"))