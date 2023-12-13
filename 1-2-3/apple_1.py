#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drawing():
  drawer.color("red")
  drawer.write("A", font = ("arial", 55, "bold"))

def falling():
  apple.right(90)
  apple.penup()
  apple.forward(130)
  apple.pendown()

if wn.onkeypress(drawing, "a") == True:
  falling()

wn.listen()

'''
if wn.onkeypress(drawing, "A"):
  falling()
'''


#-----function calls-----
draw_apple(apple)
wn.bgpic("background.gif")
wn.mainloop()








