from turtle import *

DAN = Turtle()
screen = DAN.getscreen()
DAN.forward(100)


def printname():
	name = screen.textinput("name","what is your name?")
	DAN.write(name,move=true,align="left",fonts=("Arial", 40, "bold"))
	screen.listen()

screen.onkey(printname,"1")

screen.listen()
screen.mainloop()

