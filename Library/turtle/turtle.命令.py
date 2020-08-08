import turtle
turtle.width(10)   # 笔的宽度
turtle.showturtle()  # 显示箭头
turtle.write("锡权")
turtle.forward(300)  # 前进300像素
turtle.color('red')  # 画笔颜色改为red
turtle.left(90)      # 夹头左转90度
turtle.forward(300)
turtle.goto(0, 50)  # 去坐标（0，50）
turtle.goto(0, 0)
turtle.penup()  # 抬笔，这样路径没有画线
turtle.goto(0, 300)
turtle.goto(0, 0)
turtle.pendown()    # 下笔，路径有画线
turtle.goto(50, 50)

turtle.circle(100)  # 画圆



