"""
开发者自定义一种“有内涵”的语言（或者叫字符串），并设定相关的解释规则，输入该字符串后可以输出公认的解释，或者执行程序可以理解的动作。
应用场景：编译器、运算表达式计算、SQL解析、符号处理
解释器模式要实现两个核心角色：
终结符表达式：实现与文法中的元素相关联的解释操作，通常一个解释器模式中只有一个终结符表达式，但有多个实例，对应不同的终结符。终结符一半是文法中的运算单元，比如有一个简单的公式R=R1+R2，在里面R1和R2就是终结符，对应的解析R1和R2的解释器就是终结符表达式。
非终结符表达式：文法中的每条规则对应于一个非终结符表达式，非终结符表达式一般是文法中的运算符或者其他关键字，比如公式R=R1+R2中，+就是非终结符，解析+的解释器就是一个非终结符表达式。非终结符表达式根据逻辑的复杂程度而增加，原则上每个文法规则都对应一个非终结符表达式。
主要解决：对于一些固定文法构建一个解释句子的解释器。
何时使用：如果一种特定类型的问题发生的频率足够高，那么可能就值得将该问题的各个实例表述为一个简单语言中的句子。这样就可以构建一个解释器，该解释器通过解释这些句子来解决该问题。
应用实例：编译器、运算表达式计算。
优点： 1、可扩展性比较好，灵活。 2、增加了新的解释表达式的方式。 3、易于实现简单文法。
缺点： 1、可利用场景比较少。 2、对于复杂的文法比较难维护。 3、解释器模式会引起类膨胀。

"""
import time
import datetime


class Code:
    def __init__(self, text=None):
        self.text = text


class InterpreterBase:
    def run(self, code):
        pass


class Interpreter(InterpreterBase):
    def run(self, code):
        code = code.text
        code_dict = {'获取当前时间戳': time.time(), '获取当前日期': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        print(code_dict.get(code))


if __name__ == '__main__':
    test = Code()
    test.text = '获取当前时间戳'
    Interpreter().run(test)
    test.text = '获取当前日期'
    Interpreter().run(test)
