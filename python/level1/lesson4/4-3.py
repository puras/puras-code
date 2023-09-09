import turtle

turtle.shape('turtle')
turtle.speed(0)

size = 70
x = 70
y = 160

turtle.pencolor('pink')

# 头部
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(160)
turtle.end_fill()

# 眼睛
turtle.penup()
turtle.goto(-x, y)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(size)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(size)
turtle.end_fill()

# 眼珠
size = 15
x = 30
y = 220
turtle.pencolor('black')
turtle.penup()
turtle.goto(-x, y)
turtle.pendown()
turtle.dot(size)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot(size)

turtle.penup()
turtle.goto(0, -65)
turtle.pendown()
turtle.write('粉色大眼怪', align='center', font=('楷体', 45))

name = turtle.textinput('作者', '请输入你的名字')
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.write('小画家: ' + name, align='center', font=('楷体', 20))

turtle.hideturtle()
turtle.done()
