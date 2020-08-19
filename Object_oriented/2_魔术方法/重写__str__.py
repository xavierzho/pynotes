# 在将对象转换成字符串 str(object) 测试的时候，打印对象的信息


class Person:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 也是实例方法
        """
        打印对象 自定义对象 改变输出的内容格式
        """
        return "名字是:{0} 年龄:{1}".format(self.name, self.age)


p = Person('zxq', 20)
print(p)





