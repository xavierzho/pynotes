class MysingLenton:

    __obj = None    # 类属性
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if MysingLenton.__init_flag:
            print("init...")
            self.name = name
            MysingLenton.__init_flag = False


a = MysingLenton("aa")
b = MysingLenton("bb")
print(a)
print(b)
c = MysingLenton("cc")
print(c)


