# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
wn = trtl.Screen()

#-----game configuration----
box_color = "black"

#-----initialize turtle-----

#setup for box
box = trtl.Turtle()
box.color(box_color)
box.shape("square")
box.shapesize(4)
box.fillcolor("blue")
box.penup()
score = int(0)

#setup for score writer
scorewriter = trtl.Turtle()
scorewriter.penup()
scorewriter.goto(-450, -375)
font_setup = ("Arial", 20, "normal")

#setup for timer
counter =  trtl.Turtle()
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter.penup()
counter.goto(-400, -350)

#-----game functions--------

def change_position():
    x = rand.randint(1,400)
    y = rand.randint(1,300)
    box.goto(x,y)
    new_xpos = x
    new_ypos = y
    box.goto(new_xpos, new_ypos)
    upscore()

def upscore():
    global score
    score += 1
    scorewriter.clear()
    print(scorewriter.write(score, font = font_setup))

def box_clicked(x, y):
    change_position()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
box.onclick(box_clicked)
wn.ontimer(countdown, counter_interval)
trtl.Screen()
wn.mainloop()

