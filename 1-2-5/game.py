import turtle as trtl
wn = trtl.Screen()
runner = trtl.Turtle()
box = trtl.Turtle()
wn.bgpic("bg2.gif")
runner.penup()

#turtle position setup
runner.right(180)
runner.forward(420)
runner.right(180)

#box setup
box.penup()
box.shape("square")
box.shapesize(1)
box.goto(400,-50)
boxxposition = 400
boxyposition = -50

def win():
    if runner.xcor == box:
        print("you win")
    if runner.ycor() == box:
        print("you win")

#keypress
def w():
    runner.forward(20)
    win()

def s():
    runner.back(20)
    win()

def a():
    runner.left(45)
    win()

def d():
    runner.right(45)
    win()


#listen for keypress
wn.onkeypress(w, "w")
wn.onkeypress(s, "s")
wn.onkeypress(a, "a")
wn.onkeypress(d, "d")

wn.listen()
wn.mainloop()