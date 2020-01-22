import turtle as t

t.shape('turtle')

t.speed(1)

for i in range(10):
    if i % 2 == 0:
        t.fd(100)
        t.rt(144)
    if i % 2 == 1:
        t.fd(100)
        t.lt(72)
