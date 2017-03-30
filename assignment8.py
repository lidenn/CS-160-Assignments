import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()

	
def d(x,y):
	turtle.penup()
	turtle.right(90)
	turtle.forward(50)
	turtle.pendown()
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(180)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
# To make it go to next letter

	turtle.penup()
	turtle.right(90)
	turtle.forward(50)
	turtle.pendown()

def o(x,y):
	turtle.penup()
	turtle.right(90)
	turtle.forward(50)
	turtle.left(90)
	
	turtle.pendown()
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)

#Make it go to next letter
	turtle.penup()
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(100)
	turtle.pendown()
def n(x,y):
	turtle.penup()
	turtle.right(90)
	turtle.forward(50)
	turtle.pendown()
	turtle.forward(50)
	turtle.right(180)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.right(180)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.pendown()

	
def u(x,y):

	turtle.penup()
	turtle.right(90)
	turtle.forward(50)
	turtle.pendown()
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.penup()
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.pendown()
def t(x,y):
	turtle.penup()
	turtle.right(90)
	turtle.forward(30)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(50)
	turtle.left(180)
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(70)
	turtle.left(180)
	turtle.forward(100)
	turtle.penup()
	turtle.right(90)
	turtle.forward(75)
	turtle.pendown()

def s(x,y):
	turtle.penup()
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.pendown()
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(25)
	turtle.left(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(25)
	turtle.right(90)
	turtle.forward(50)

	turtle.penup()
	turtle.right(180)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.pendown()





def letters(x,y):

	again = True
	while again:
		correct = 1
		while (correct == 1):
			print ("Welcome to String Printer")
			print ("Options: D O N U T S")
			inputstring = str(input("Enter String: "))
			place=0
			for place in range (len(inputstring)):	
				if (inputstring[place] == 'D' or inputstring[place] == 'd'):
					correct=2
				elif (inputstring[place] == 'O' or inputstring[place] == 'o'):
					correct=2
				elif (inputstring[place] == 'N' or inputstring[place] == 'n'):
					correct=2
				elif (inputstring[place] == 'U' or inputstring[place] == 'u'):
					correct=2
				elif (inputstring[place] == 'T' or inputstring[place] == 't'):
					correct=2
				elif (inputstring[place] == 'S' or inputstring[place] == 's'):
					correct=2
					
				else :
					correct =1
					break;
		


		place = 1
		turtle.clear
		turtle.reset()
		for place in range (len(inputstring)):
			if (inputstring[place] == 'D' or inputstring[place] == 'd'):
				d(x,y)
			elif (inputstring[place] == 'O' or inputstring[place] == 'o'):
				o(x,y)
			elif (inputstring[place] == 'N' or inputstring[place] == 'n'):
				n(x,y)
			elif (inputstring[place] == 'U' or inputstring[place] == 'u'):
				u(x,y)
			elif (inputstring[place] == 'T' or inputstring[place] == 't'):
				t(x,y)
			elif (inputstring[place] == 'S' or inputstring[place] == 's'):
				s(x,y)
			place =+1
		print ("Use again?")
		again = input("Y to use again, N to stop: ")
		if again =="Y" or again == "y" :
			again = True
		else:
			again = False

def main():

	window.onclick(letters)






main()
window.mainloop()




