import argparse  # 自定义命令行模块

# 创建解析器对象
parser = argparse.ArgumentParser(prog='autologin', usage='%(prog)s [options] usage',
                                 description='编写自定义命令行描述信息', epilog='my-epilog')
# 添加位置参数【必选参数】
parser.add_argument('loginType', type=str, help='login type')

# 添加可选参数【】
# parser.add_argument('-s', '--sex', action='append', type=str, help='你的性别')
# 限定参数范围
parser.add_argument('-u', dest='user', type=str, help='user name')
parser.add_argument('-p', dest='pwd', type=str, help='password')
# print(parser.print_help())


res = parser.parse_args()
if res.user == 'root' and res.pwd == '1997':
    print('Login successful!')
else:
    print('Login fail!No such username or password')

