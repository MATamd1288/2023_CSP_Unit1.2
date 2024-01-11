import turtle as trtl
wn = trtl.Screen()
runner = trtl.Turtle()
box = trtl.Turtle
wn.bgpic("bg2.gif")


runner.penup()

#box turtle setup
box.shape("square")


#keypress
def w():
    runner.forward(20)

def s():
    runner.back(20)

def a():
    runner.left(45)

def d():
    runner.right(45)

#listen for keypress
wn.onkeypress(w, "w")
wn.onkeypress(s, "s")
wn.onkeypress(a, "a")
wn.onkeypress(d, "d")

wn.listen()
wn.mainloop()