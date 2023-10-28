import turtle as t

t.color('red', 'yellow')
t.speed(10)

t.begin_fill()
for _ in range(50):
    t.fd(200)
    t.lt(170)
t.end_fill()

t.ht()
t.done()