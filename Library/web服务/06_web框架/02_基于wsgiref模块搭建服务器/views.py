def index(env):
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        return f.read()


def login(env):
    with open('templates/login.html', 'r', encoding='utf-8') as f:
        return f.read()


def error(env):
    return '404 error'


def func(env):
    return 'xxx'


import datetime


def get_time(env):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %X')
    with open('templates/mytime.html', 'r', encoding='utf-8') as f:
        data = f.read()
    data = data.replace('asdasdasdad', current_time)
    return data


from jinja2 import Template


def get_dict(env):
    user_dict = {'username': 'jones', 'age': 22, 'hobby': 'study'}
    with open('templates/rederDict.html', 'r', encoding='utf-8') as f:
        data = f.read()
    tmp = Template(data)
    res = tmp.render(user=user_dict)  # 给这个页面传递了一个值，通过变量名user就能拿到user_dict
    return res


import pymysql


def get_user(env):
    # 在数据库中获取数据，传递给html页面， 借助模板语法发送给浏览器
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='1997',
                           database='tencent',
                           charset='utf8',
                           autocommit=True)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from hr limit 50'
    affect_rows = cursor.execute(sql)
    data_list = cursor.fetchall()
    # print(data_list)
    # 传递给html文件
    with open('templates/get_data.html', 'r', encoding='utf-8') as f:
        data = f.read()
    tmp = Template(data)
    res = tmp.render(user=data_list)
    return res


if __name__ == '__main__':
    get_user(111)

