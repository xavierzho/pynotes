import pymongo

try:
    # 1。链接mongodb的服务
    """集群uri：'%22mongodb%2Bsrv%3A%2F%2FTinsQua%3ASnq1997.%40tinsqua.crxp2.gcp.mongodb.net%2FWebSpider%3FretryWrites%3Dtrue%26w%3Dmajority%22'"""
    client = pymongo.MongoClient()

    # 2. 数据库
    # db = client['text']
    # 3.集合（表）
    collection = client['text']['stu']
    # 4.插入数据
    # 插入一个数据
    # collection.insert_one()
    # 插入多个数据
    # collection.insert_many()
    # 插入文件
    # one = [{'name': "张三", "age": "18"},
    #        {'name': "李四", "age": "28"},
    #        {'name': "王五", "age": "38"},
    #        {'name': "赵六", "age": "48"},
    #        {'name': "顺七", "age": "58"}
    #        ]
    # one = [{'name': '张三', "age": "58"},
    #               {'name': '张三', "age": "28"},
    #               {'name': '张三', "age": "38"},
    #               {'name': '张三', "age": "48"}]
    # collection.insert_many(one)
    # 删除一个
    # collection.delete_one({'age': '15'})
    # 删除多个
    # collection.delete_many({'age': "28"})
    # 修改一个数据
    # collection.update_one({'name': "顺七"}, {"$set": {"age": "50"}})
    # 修改多个数据
    # collection.update({'name': '张三'}, {"$set": {"age": '5'}})
    # 查询
    collection.find()

except Exception as e:
    print(e)
# 5.关闭数据库
finally:
    client.close()
