"""
“行为请求者”与“行为实现者”通常呈现一种“紧耦合”。但在某些场合，比如要对行为进行“记录、撤销/重做、事务”等处理，这种无法抵御变化的紧耦合是不合适的。在这种情况下，如何将“行为请求者”与“行为实现者”解耦？将一组行为抽象为对象，实现二者之间的松耦合。这就是命令模式（Command Pattern）

命令模式应该有一下几个角色：
Command：定义命令的接口，声明执行的方法，可以理解为一个基类。
ConcreteCommand：命令接口实现对象，通常会持有接收者，并调用接收者的功能来完成命令要执行的操作。
Receiver：接收者，真正执行命令的对象。任何类都可能成为一个接收者，只要它能够实现命令要求实现的相应功能。
Invoker：要求命令对象执行请求，通常会持有命令对象，可以持有很多的命令对象，相当于使用命令对象的入口。
Client：创建具体的命令对象，组装命令对象和接收者，或许，把这个Client称为装配者会更好理解，因为真正使用命令的客户端是从Invoker来触发执行。

命令模式的几个核心角色及其分工：
Command（命令基类）：主要声明抽象命令类的接口
ConcreteCommand（命令实现）：复写基类中声明的接口，实现具体的调用功能
Receiver（命令的内容）：具体执行动作的对象
Invoker(命令调度和执行)：全部命令的执行和调度入口
Client（命令装配者）:创建具体的命令对象，组装命令对象和接收者
"""


class Command:
    """声明命令模式接口"""

    def __init__(self, obj):
        self.obj = obj

    def execute(self):
        pass


class ConcreteCommand(Command):
    """实现命令模式接口"""

    def execute(self):
        self.obj.run()


class Invoker:
    """接收命令并执行的接口"""

    def __init__(self):
        self._commands = []

    def add_command(self, cmd):
        self._commands.append(cmd)

    def remove_command(self, cmd):
        self._commands.remove(cmd)

    def run_command(self):
        for cmd in self._commands:
            cmd.execute()


class Receiver:
    """具体动作"""

    def __init__(self, word):
        self.word = word

    def run(self):
        print(self.word)


def client():
    """装配者"""
    test = Invoker()
    cmd1 = ConcreteCommand(Receiver('命令一'))
    test.add_command(cmd1)
    cmd2 = ConcreteCommand(Receiver('命令二'))
    test.add_command(cmd2)
    cmd3 = ConcreteCommand(Receiver('命令三'))
    test.add_command(cmd3)
    test.run_command()


if __name__ == '__main__':
    client()