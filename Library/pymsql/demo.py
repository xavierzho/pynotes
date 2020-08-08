import pymysql

try:
    # 1.链接数据库 链接对象 connection()
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        db='school',
        user='root',
        passwd='1997',
        charset='utf8'
    )

    # 2.创建游标对象 cursor()
    cur = conn.cursor()

    # 3.插入数据
    # 开启事务
    # insert_sub = 'insert into subjects values(0,"GO语言")'
    # result = cur.execute(insert_sub)

    # 修改数据
    # update_sub = 'update subjects set title="区块链" where id=5'
    # result = cur.execute(update_sub)

    # 删除数据
    # delete_stu = 'delete from stu where id=8'
    # result = cur.execute(delete_stu)

    # 查询数据
    select_sub = 'select * from subjetcts where id=1'
    cur.execute(select_sub)
    # result = cur.fetchall()  # 返回一个集合
    result = cur.fetchone()  # 返回一个元组


    # 提交事务
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()
except Exception as e:
    print(e)

