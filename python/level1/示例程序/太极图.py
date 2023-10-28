import turtle as t

t.circle(100, 180)
t.circle(200, 180)
t.circle(100, -180)

t.fillcolor('black')

t.begin_fill()

t.circle(100, 180)
t.circle(200, 180)
t.circle(100, -180)

t.end_fill()

t.pu()

t.goto(0, 100)

t.dot(50)

t.goto(0, -100)

t.pencolor('white')
t.dot(50)

t.ht()
t.done()