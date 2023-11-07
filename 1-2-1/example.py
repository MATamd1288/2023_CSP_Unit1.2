import turtle as trtl

def drawTriangle(Long, x, y):
    test.penup()
    test.goto(x, y)
    test.pendown()
    test.fd(Long)
    test.right(120)
    test.fd(Long)
    test.right(120)
    test.fd(Long)

x = 100
y = 100
length = 43
for tri in range(100):
    drawTriangle(length, x, y)
    x += length * 1.25
    y += length * 1.25


wn = trtl.Screen()
wn.mainloop()