# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
wn = trtl.Screen()


#-----game configuration----
box_color = "black"


#-----initialize turtle-----
box = trtl.Turtle()
box.color(box_color)
box.shape("square")
box.shapesize(4)
box.fillcolor("blue")


#-----game functions--------
def box_clicked(x, y):
    print("box was clicked!")
    change_position()

def change_position():
    x = rand.randint(1,400)
    y = rand.randint(1,300)
    box.goto(x,y)
    new_xpos = x
    new_ypos = y


#-----events----------------
box.onclick(box_clicked)
trtl.Screen()
wn.mainloop()

