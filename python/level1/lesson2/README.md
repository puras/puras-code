第二课内容
----

# 坐标
* 理解直解坐标系与坐标值
* 画布中心点就等于坐标系的中心点(0, 0)

# 新方法
* goto(x, y) 跳转到指定坐标位置，示例turtle.goto(0, 0)
* penup() 画笔抬起，示例turtle.penup()
* pendown() 画笔落下，示例turtle.pendown()

# 程序示例
* 同心圆

    import turtle

    turtle.shape('turtle')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(100)

* 并排圆
    import turtle

    turtle.shape('turtle')
    
    turtle.circle(100)
    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    turtle.circle(100)

* 爱睡觉的小呆
    
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