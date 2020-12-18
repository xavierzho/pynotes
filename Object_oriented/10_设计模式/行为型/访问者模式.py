"""
访问者模式，数据结构中保存着许多元素，当改变一种对元素的处理方式但时，我们避免重复的修改数据类的结构，那我们在设计之初就将数据的处理分离，即数据类只提供一个数据处理的接口，而数据类的处理方法我们叫它访问者，那么相同结构的数据面临不同的处理结果时，我们只需要创建不同的访问者。
访问者模式作为常用设计模式中难度最大的一种模式，他的难度在于高度的抽象，及其多层嵌套
"""


class Finance:
    """财务数据结构类"""

    def __init__(self):
        self.sales_volume = None  # 销售额
        self.cost = None  # 成本
        self.history_sales_volume = None  # 历史销售额
        self.history_cost = None  # 历史成本

    def set_sales_volume(self, value):
        self.sales_volume = value

    def set_cost(self, value):
        self.cost = value

    def set_history_sales_volume(self, value):
        self.history_sales_volume = value

    def set_history_cost(self, value):
        self.history_cost = value

    def accept(self, visitor):
        pass


class FinanceYear(Finance):
    """年度财报数据类"""

    def __init__(self, year):
        Finance.__init__(self)
        self.work = []
        self.year = year

    def add_work(self, work):
        self.work.append(work)

    def accept(self):
        for obj in self.work:
            obj.visit(self)


class Accounting:
    """会计类"""
    def __init__(self):
        self.ID = '会计'
        self.Duty = '计算报表'

    def visit(self, table):
        print(f'会计年度：{table.year}')
        print(f'我的身份是：{self.ID}|职责：{self.Duty}')
        print(f'本年度纯利润：{table.sales_volume - table.cost}')
        print('----------------')


class Audit:
    """财务总监类"""

    def __init__(self):
        self.ID = '财务总监'
        self.Duty = '分析业务'

    def visit(self, table):
        print(f'会计总监年度：{table.year}')
        print(f'我的身份是：{self.ID}|职责：{self.Duty}')
        if table.sales_volume - table.cost > table.history_sales_volume - table.history_cost:
            msg = '较同期上涨'
        else:
            msg = '较同期下跌'
        print(f'本年度公司业绩：{msg}')
        print('----------------')


class Adviser:
    """战略顾问类"""

    def __init__(self):
        self.ID = '战略顾问'
        self.Duty = '制定明年战略'

    def visit(self, table):
        print(f'战略顾问年度：{table.year}')
        print(f'我的身份是：{self.ID}|职责：{self.Duty}')
        if table.sales_volume > table.history_sales_volume:
            msg = '行业上行，扩大生产规模'
        else:
            msg = '行业下行，缩小生产规模'
        print(f'本年度公司业绩：{msg}')
        print('----------------')


class Work:
    """工作类"""

    def __init__(self):
        self.works = []

    def add_work(self, obj):
        self.works.append(obj)

    def remove_work(self, obj):
        self.works.remove(obj)

    def visit(self):
        for obj in self.works:
            obj.accept()


if __name__ == '__main__':
    work = Work()
    finance_2020 = FinanceYear(2020)
    finance_2020.set_sales_volume(200)
    finance_2020.set_cost(100)
    finance_2020.set_history_sales_volume(180)
    finance_2020.set_history_cost(90)
    accounting = Accounting()
    audit = Audit()
    adviser = Adviser()
    finance_2020.add_work(accounting)
    finance_2020.add_work(audit)
    finance_2020.add_work(adviser)
    work.add_work(finance_2020)
    work.visit()
