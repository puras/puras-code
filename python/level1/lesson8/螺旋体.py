import turtle as t

t.shape('turtle')
t.speed(10)

x = 0

for i in range(200):
    t.fd(x)
    t.rt(12)
    x += 0.1

t.hideturtle()
t.done()