import pymysql

conn_info = {
    "host": "192.168.2.140",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "test"
}
db = pymysql.connect(**conn_info)

with db:
    # with db.cursor() as cursor:
        # Create a new record
    #     sql = "INSERT INTO `test0` (`id`,`name`,`age`) VALUES (%s,%s,%s)"
    #     cursor.execute(sql, ("2", 'pinksale', "22",))
    #
    # # db is not autocommit by default. So you must commit to save
    # # your changes.
    # db.commit()

    with db.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `test0` WHERE `id`= %s"
        cursor.execute(sql, ("1",))
        result = cursor.fetchone()
        print(result)
