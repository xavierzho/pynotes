"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/29
"""
import pymongo
import datetime
import re

client = pymongo.MongoClient(host='localhost', port=27017)
collection = client['news']['caijing']

# for doc in collection.find():
#     if "time" in doc:
#         if doc['time'].startswith("2020"):
#             print(doc['time'])
#         else:
#             res = collection.update_one(doc, {"$set": {'time': "2020-"+doc['time']}})
#             print(res)
#     else:
#         collection.update_one(doc, {"$set": {'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})

# for doc in collection.find():
#     if "nav_link" in doc:
#         if "hbrchina" in doc['nav_link']:
#             collection.delete_one(doc)
#         else:
#             pass
#     else:
#         pass

# for doc in collection.find():
#     if 'desc' in doc:
#         if doc['desc']:
#             if re.match("^[\u4e00-\u9fff]|【", doc['desc']):
#                 pass
#             else:
#                 collection.update_one(doc, {"$set": {'desc': None}})
#
# print(collection.distinct("news_id").count("news_id"))


# for i in iter(collection.distinct("news_id")):
#     news_id_obj = collection.find(({"news_id": i}))
#     count = news_id_obj.count()
#     if count > 1:
#         for j in news_id_obj.limit(count - 1):
#             collection.delete_one(j)

for i in collection.aggregate([
    {"$group": {"_id": None, "distinct": {"$addToSet": "$news_id"}}},
    {"$project": {"_id": 0, "img": 0, "content": 0, "title_link": 0}}
]):
    print(i)
client.close()
