import turtle

turtle.shape('turtle')

# 画头
turtle.circle(150)

# 左眼
turtle.penup()
turtle.goto(-70, 220)
turtle.pendown()
turtle.forward(50)

# 右眼
turtle.penup()
turtle.goto(70, 220)
turtle.pendown()
turtle.forward(50)

# 嘴巴
turtle.penup()
turtle.goto(40, 70)
turtle.pendown()
turtle.circle(60)

# 鼻孔
# 左
turtle.penup()
turtle.goto(15, 115)
turtle.pendown()
turtle.circle(15)

# 右
turtle.penup()
turtle.goto(65, 115)
turtle.pendown()
turtle.circle(15)

turtle.hideturtle()

turtle.done()
