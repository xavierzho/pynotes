import pymysql


class MySQL:

    def __enter__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', '1997', 'myblog')
        # cursor=pymysql.cursors.DictCursor 查出来的信息使用字典显示
        self.cour = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return self.cour

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.cour.close()
            self.conn.close()
        except:
            print(exc_type)
            print(exc_val)
            print(exc_tb)


with MySQL() as cour:
    sql = 'select id,username from main_users'
    cour.execute(sql)
    res = cour.fetchall()
    for i in res:
        print(i)


