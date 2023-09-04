第三课内容
----

# 变量
* 变量像一个魔术盒子，可以把任何想要的东西放进去
* 结构：变量名 = 变量值（表达式），中间的等号是赋值号，与数学中的等号不同
* 命名规则：1、必段是英文、数字和下划线的组合，且不能以数字开头；2、不能包含空格；3、关键字和函数名不能作为变量名；4、应简短且具描述性

# 代码注释
* 添加文字说明，增加代码的条理性与可读性
* 注释是增加#号，后面加描述内容

# 新命令
* ctrl+c 复制
* ctrl+v 粘贴

# 新方法
* dot(半径) 绘制实心圆，示例turtle.dot(15)
* speed(速度) 调整绘制速度，0：最快，1-10，逐渐加快，空：返回当前速度，示例turtle.speed(5)
* pencolor(颜色) 设置绘制线条的颜色，示例turtle.pencolor('red')
* fillcolor(颜色) 设置填充色，示例turtle.fillcolor('red')
* begin_fill() 填充开始位置
* end_fill() 填充结束位置

# 程序示例
* 变量
``` 
import turtle

turtle.shape('turtle')

# length = 100
length = 200

turtle.forward(length)
turtle.left(90)

turtle.forward(length)
turtle.left(90)

turtle.forward(length)
turtle.left(90)

turtle.forward(length)
turtle.left(90)
```
* 大眼怪
```
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
```

* 带颜色的大眼怪

```
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
```