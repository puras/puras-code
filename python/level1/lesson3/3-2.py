import turtle

turtle.shape('turtle')
turtle.speed(7)

size = 70
x = 70
y = 160

# 头部
turtle.circle(160)

# 眼睛
turtle.penup()
turtle.goto(-x, y)
turtle.pendown()
turtle.circle(size)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(size)

# 眼珠
size = 15
x = 30
y = 220
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
