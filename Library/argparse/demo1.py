import argparse  # 自定义命令行模块

# 创建解析器对象
parser = argparse.ArgumentParser(prog='命令行名', usage='%(prog)s [options] usage',
                                 description='编写自定义命令行描述信息', epilog='my-epilog')
# 添加位置参数【必选参数】
parser.add_argument('name', type=str, help='你自己的名字')
parser.add_argument('age', type=int, help='你自己的年龄')
# 添加可选参数【】
# parser.add_argument('-s', '--sex', action='append', type=str, help='你的性别')
# 限定参数范围
parser.add_argument('-s', '--sex', default='男', choices=['男', '女', 'Female', 'Male'],
                    action='append', type=str, help='你的性别')
# print(parser.print_help())


res = parser.parse_args()

print(res.name, res.age, res.sex)
