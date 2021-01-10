"""
用于计算公司员工的薪资
"""


company = "北京尚学堂"


def yearSalary(monthSalary):
    """根据输入的月薪的值，计算出年薪：monthSalary*12"""
    return monthSalary*12


def daySalary(monthSalary):
    """根据传入的月薪值，计算出1天的薪资，一个月按照22.5天计算（国家规定的工作日）"""
    return monthSalary/22.5


if __name__ =="__main__":  # 模块独立运行
    print(yearSalary(3000))
    print(daySalary(3000))
