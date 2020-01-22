import turtle as t

t.shape('turtle')
t.color('#0055FF')

n = int(input())

t.begin_fill()

for i in range(n):
    t.rt(360/n)
    t.fd(100)

t.end_fill()

