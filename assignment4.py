again = 1
while (again==1):

	print ("Press 1 for Scientific Mode, Press 2 for Decimal to Binary, Press 3 for Binary to Decimal")
	calculator = int(input("Enter number: "))
	
	
	if calculator==1:
		print("Press 1 to add, Press 2 to subtract, Press 3 to multiply, Press 4 to divide, Press 5 to exponeniate")
		operation = int(input("Enter number: "))
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		if operation ==1:
			print("Answer: ",num1,"+",num2,"=",num1+num2)
		if operation ==2:
			print("Answer: ",num1,"-",num2,"=",num1-num2)
		if operation ==3:
			print("Answer: ",num1,"*",num2,"=",num1*num2)
		if operation ==4:
			print("Answer: ",num1,"/",num2,"=",num1/num2)
		if operation ==5:
			print("Answer: ",num1,"**",num2,"=",num1**num2)
	

	if calculator==2:
		print ("Decimal to Binary")
		y = int(input("Enter decimal number:"))
		if y>=0:
			i=0
			binary=0
			rem=y%2
			y=y//2
			binary=binary+(rem*(10**i))
			i+=1
			print (binary)
		if y<0:
			print("Please input a positive integer")



	if calculator==3:
		print ("Binary to Decimal")
		bin3=int(input("Enter Binary Number: "))
		z=0
		decimal=0
		while bin3>0:
			rem3=bin3%10
			bin3=bin3//10
			decimal=decimal+(rem3*(2**z))
			z+=1
		print (decimal)
				
	
	else:
		print("Please input 1 or 2")
	
	print ("Would you like to use again?")
	again = int(input("Press 1 to use again, Press 2 to stop "))
