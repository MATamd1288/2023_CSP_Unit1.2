import turtle as trtl

maze_painter = trtl.Turtle()

x = 20
y = 20
number = 28
path_width = 10
pencolor = ("black")

maze_painter.speed(0)

for loop in range(29):
    maze_painter.left(90)
    maze_painter.forward(x)
    x += y

    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()

    maze_painter.left(90)
    maze_painter.forward(path_width * 4)
    maze_painter.back(path_width * 4)
    maze_painter.right(90)



wn = trtl.Screen()
wn.mainloop()