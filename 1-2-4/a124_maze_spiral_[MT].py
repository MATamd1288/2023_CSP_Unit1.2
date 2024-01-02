'''

x = starting distance
y = incremental distance

For loop in range (amt of times)
    move forward

    turn right

    go x + y

'''

import turtle as trtl

pen = trtl.Turtle()

x = 20
y = 20

pen.speed(0)

for loop in range(29):
    pen.left(90)
    pen.forward(x)
    x += y

wn = trtl.Screen()
wn.mainloop()