import pymongo

# 创建MongoDB客户端对象
client = pymongo.MongoClient(host="localhost", port=27017)

# 链接数据库
db = client["newdbname"]

# 获取名为newtablename的数据表，插入一条数据
db["newtablename"].insert_one({"name": "heiheihei", "age": 21})

# 查询数据
info = db["newtablename"].find_one({"age": 21})
print(info)