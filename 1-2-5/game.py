import turtle as trtl
import time
wn = trtl.Screen()
runner = trtl.Turtle()
box = trtl.Turtle()
wn.bgpic("bg2.gif")

#turtle position setup
runner.penup()
runner.right(180)
runner.forward(420)
runner.right(180)

#box setup
box.penup()
box.shape("square")
box.shapesize(5)
box.goto(400, -50)

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

#Game win event
def win():
    if runner.xcor() >= 400:
        print("you win")

        print("It took", start - end, "seconds!")

    if runner.ycor() >= 20:
        print("you win")
        print("It took", start - end, "seconds!")

# Calculate the start time
start = time.time()

# Code here

# Calculate the end time and time taken
end = time.time()
length = start - end


#listen for keypress
wn.onkeypress(w, "w")
wn.onkeypress(s, "s")
wn.onkeypress(a, "a")
wn.onkeypress(d, "d")

wn.listen()
wn.mainloop()