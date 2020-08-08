# 导入随机数库
import random
# 从控制台输入要出的拳头 --石头（1）/剪刀（2）/布（3）
player = int(input("请输入您要出的拳石头（1）/剪刀（2）/布（3）:"))

# 电脑随机出拳--先假定电脑只出石头，完成整体代码构建
computer = random.randint(1, 3)


print("玩家出的是拳头 %d -电脑出的拳头是 %d" % (player, computer))
# 比较出胜负
"""
石头 胜 剪刀
剪刀 胜 布
布 胜 石头
"""
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("电脑太弱了！")
# 平局
elif player == computer:
    print("哟，我们一样哎！再来一盘！")

# 其他情况就是电脑获胜
else:
    print("哦吼，你输了！")
