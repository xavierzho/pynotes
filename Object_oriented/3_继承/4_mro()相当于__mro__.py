class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say AAA!")


class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB!")


class C(B, A):
    def cc(self):
        print("cc")

    def cc(self):
        print("cc")


c = C()
c.cc()
c.bb()
c.aa()
print(C.mro())      # 打印类的层次结构
c.say()  # 解释器寻找方法是"从左到右"的方式寻找,此时会执行B类钟的say.

print(c.__dict__)
print(c.__class__)
print(C.__bases__)
print(C.mro())
print(A.__subclasses__())