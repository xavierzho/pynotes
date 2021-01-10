class AgeError(Exception):  # 继承Exception类
    def __init__(self, errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo

    def __str__(self):
        return self.errorInfo+"年龄错误！应该在1-150之间"


if __name__ == "__main__":  # 如果为True,则模块是作为独立文件执行，可以执行测试代码
    age = int(input("请输入一个年龄："))
    if age < 1 or age > 150:
        raise AgeError
    else:
        print("正常的年龄：", age)

