import turtle as t

t.speed(10)

for i in range(360):
    t.setheading(i) # 设置朝向
    for i in range(4):
        t.fd(100)
        t.lt(90)

t.ht()
t.done()