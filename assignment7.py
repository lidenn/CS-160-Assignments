def d():
	print ("*** ")
	print ("*  *")
	print ("*  *")
	print ("*  *")
	print ("*** ")
	print ("    ")

def o():
	print (" ** ")
	print ("*  *")
	print ("*  *")
	print ("*  *")
	print (" ** ")
	print ("    ")

def n():
	print ("*  *")
	print ("*  *")
	print ("** *")
	print ("* **")
	print ("*  *")
	print ("    ")

def u():
	print ("*  *")
	print ("*  *")
	print ("*  *")
	print ("*  *")
	print ("****")
	print ("    ")

def t():
	print ("*** ")
	print (" *  ")
	print (" *  ")
	print (" *  ")
	print (" *  ")
	print ("    ")

def s():
	print (" ***")
	print ("*   ")
	print (" ** ")
	print ("   *")
	print ("*** ")
	print ("    ")

def main():
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

					
			



		place = 0
		for place in range (len(inputstring)):
			if (inputstring[place] == 'D' or inputstring[place] == 'd'):
				d()
			elif (inputstring[place] == 'O' or inputstring[place] == 'o'):
				o()
			elif (inputstring[place] == 'N' or inputstring[place] == 'n'):
				n()
			elif (inputstring[place] == 'U' or inputstring[place] == 'u'):
				u()
			elif (inputstring[place] == 'T' or inputstring[place] == 't'):
				t()
			elif (inputstring[place] == 'S' or inputstring[place] == 's'):
				s()
			place +=1
		print ("Use again?")
		again = input("Y to use again, N to stop: ")
		if again =="Y" or again == "y" :
			again = True
		else:
			again = False

main()
