import turtle

t = turtle.Pen()


t.speed(0)
for i in range(21):
    t.penup()
    t.goto(0, i*20)
    t.pendown()
    t.goto(400, i*20)

for i in range(21):
    t.penup()
    t.goto(i*20, 0)
    t.pendown()
    t.goto(i*20, 400)


turtle.done()

