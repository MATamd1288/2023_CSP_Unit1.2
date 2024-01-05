#   a123_apple_1.py
import turtle as trtl
import random as rand
# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic("background.gif")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
List = []
Letters = []
for i in range(5):
  apple2 = trtl.Turtle()
  List.append(apple2)
  Letters.append(rand.choice(alphabet))
# -----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  List[index].penup()
  List[index].shape(apple_image)
  wn.tracer(False)
  List[index].setx(rand.randint(-150, 150))
  List[index].sety(rand.randint(-40, 150))
  List[index].sety(List[index].ycor() - 37)
  List[index].color("white")
  List[index].write(Letters[index], align='center', font=("Arial", 55, "bold"))
  List[index].sety(List[index].ycor() + 37)
  List[index].showturtle()
  wn.tracer(True)
  wn.update()
def falling(index):
  List[index].penup()
  List[index].clear()
  List[index].goto(0, -150)
  List[index].hideturtle()
  draw_apple(index)
def A():
  for i in range(5):
    if Letters[i] == "a":
      falling(i)
def S():
  for i in range(5):
    if Letters[i] == "s":
      falling(i)
def D():
  for i in range(5):
    if Letters[i] == "d":
      falling(i)
def F():
  for i in range(5):
    if Letters[i] == "f":
      falling(i)
def G():
  for i in range(5):
    if Letters[i] == "g":
      falling(i)
def H():
  for i in range(5):
    if Letters[i] == "h":
      falling(i)
def J():
  for i in range(5):
    if Letters[i] == "j":
      falling(i)
def K():
  for i in range(5):
    if Letters[i] == "k":
      falling(i)
def L():
  for i in range(5):
    if Letters[i] == "l":
      falling(i)

def Q():
  for i in range(5):
    if Letters[i] == "q":
      falling(i)

def W():
  for i in range(5):
    if Letters[i] == "w":
      falling(i)

def E():
  for i in range(5):
    if Letters[i] == "e":
      falling(i)

def R():
  for i in range(5):
    if Letters[i] == "r":
      falling(i)

def T():
  for i in range(5):
    if Letters[i] == "t":
      falling(i)

def Y():
  for i in range(5):
    if Letters[i] == "y":
      falling(i)

def U():
  for i in range(5):
    if Letters[i] == "u":
      falling(i)

def I():
  for i in range(5):
    if Letters[i] == "i":
      falling(i)

def O():
  for i in range(5):
    if Letters[i] == "o":
      falling(i)

def P():
  for i in range(5):
    if Letters[i] == "p":
      falling(i)

def Z():
  for i in range(5):
    if Letters[i] == "z":
      falling(i)

def X():
  for i in range(5):
    if Letters[i] == "x":
      falling(i)

def C():
  for i in range(5):
    if Letters[i] == "c":
      falling(i)

def V():
  for i in range(5):
    if Letters[i] == "v":
      falling(i)

def B():
  for i in range(5):
    if Letters[i] == "b":
      falling(i)

def N():
  for i in range(5):
    if Letters[i] == "n":
      falling(i)

def M():
  for i in range(5):
    if Letters[i] == "m":
      falling(i)

# -----function calls-----
for i in range(5):
  draw_apple(i)

wn.onkeypress(S, "s")
wn.onkeypress(D, "d")
wn.onkeypress(F, "f")
wn.onkeypress(G, "g")
wn.onkeypress(H, "h")
wn.onkeypress(J, "j")
wn.onkeypress(K, "k")
wn.onkeypress(L, "l")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
