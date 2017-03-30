import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()

def star(x,y):
	turtle.clear
	turtle.reset()

	for i in range(5):
		turtle.forward(300)
	turtle.right(144)
	

window.onclick(star)


window.mainloop()
