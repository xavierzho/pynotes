import mysql.connector

conn = mysql.connector.connect(
    host='localhost',  # 数据库主机地址
    user='root',  # 数据库用户名
    passwd='1997',  # 数据库密码
    db='cov-19'
)

cur = conn.cursor()
sql = 'select * from international'
cur.execute(sql)
print(cur.fetchall())

