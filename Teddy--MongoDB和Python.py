from pymongo import MongoClient


client = MongoClient('localhost', 27017)
# 连接test数据库，没有则自动创建
db = client.test
# 使用zyp集合，没有则自动创建
my_set = db.zyp

my_set.insert_one({"name":"carina","age":18,"job":"software test"})
