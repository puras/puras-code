import turtle as t

t.shape('turtle')
t.speed(10)
len = 1

for i in range(200):
    t.fd(len)
    t.lt(90)

    len += 2

t.ht()
t.done()