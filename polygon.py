import turtle as tr
tr.Screen().bgcolor("green")
pl = tr.Turtle()

sides = 3
length = 80

angle = 360 / sides

for i in range(sides):
    pl.forward(length)
    pl.right(angle)

tr.done()