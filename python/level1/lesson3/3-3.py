import turtle

turtle.shape('turtle')
turtle.speed(7)

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

turtle.hideturtle()
turtle.done()
