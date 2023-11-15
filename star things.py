strlvl = ("*")

def star ():
    global strlvl
    for level in range(5):
        print(strlvl)
        strlvl = strlvl + ("*")

star()