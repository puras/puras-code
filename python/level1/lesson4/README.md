第四课数据类型与转换
----

# 字符串

字符串是由单引号或双引号括起来的一串字符

## 创建

* 单引号或双引号均可(英文状态下)
* 引号统一，不能单、双引号混用

## 加法-拼接

加号相当于两个字符串拼接，两个串合并

# 数据类型

* 数字类型
  * int 整型
  * float 浮点型
* 字符串类型 
  * string

# 转换

* int 向下取整，去掉小数部分的数值，得到整类类型
* str 将其他数据类型转换为字符串类型
* 字符串中包含非数字，无法转换成int

# 新方法
* print(内容) # 打印内容，打完结束会自动换行
* type(变量) # 查看变量属于什么数据类型
* textinput(标题, 提示) # 弹出输入框，展示标题和提示信息，用户可输入内容，将内容赋值给左侧的变量

# 程序示例

* 粉色大眼怪

```python
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
```

