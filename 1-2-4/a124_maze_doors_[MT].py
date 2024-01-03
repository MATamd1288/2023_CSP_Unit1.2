'''
import turtle as trtl
import random as rand

maze_painter = trtl.Turtle()
randnum = rand

x = 20
y = 20
path_width = 10
pencolor = ("black")

def door():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()

def barrier():
    maze_painter.forward(40)
    maze_painter.right(90)
    maze_painter.forward(path_width * 2)
    maze_painter.back(path_width * 2)
    maze_painter.left(90)

maze_painter.speed(0)

for loop in range(29):
    maze_painter.left(90)
    maze_painter.forward(x)
    x += y

wn = trtl.Screen()
wn.mainloop()
'''

import turtle as trtl

# maze configuration variables
num_sides = 25
path_width = 15
wall_color = "blue"

# config maze
maze_painter = trtl.Turtle()
maze_painter.pensize(5)
maze_painter.pencolor(wall_color)
maze_painter.speed("fastest")

def drawSpiral():
    wall_len = path_width
    for w in range(num_sides):
        wall_len += path_width

        if (w > 4):
            # Initial turn for painter to be in the correct direction
            maze_painter.left(90)

            # Draw the door
            draw_door()

            # Draw the barrier
            draw_barrier()

            # Remember: you have to subtract the amount you drew for the wall and
            # barrier to avoid making the walls bigger.
            maze_painter.forward(wall_len - 10 - path_width - 40)

def draw_door():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()

def draw_barrier():
    # draw barrier wall
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.backward(path_width * 2)
    maze_painter.right(90)

drawSpiral()
maze_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()