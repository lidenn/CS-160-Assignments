print ("Area Under the Curve")
def f1(x):
	result = ((5*(x**4))+(3*(x**3))-(10*x)+(2))
	return result
def f2(x):
	result = ((x**2)-10)
	return result
def f3(x):
	result = (40*x+5)
	return result
def f4(x):
	result = (x**3)
	return result
def f5(x):
	result = (20*(x**2)+(10*x)-2)
	return result

def rectangle(n, a, b, f):
	total_area=0
	interval = (b-a)/n
	while (a<b):
		if (f==1):
			area=f1(a)*interval
		elif(f==2):
			area=f2(a)*interval
		elif(f==3):
			area=f3(a)*interval
		elif(f==4):
			area=f4(a)*interval
		elif(f==5):
			area=f5(a)*interval
		total_area=total_area+area
		a+=interval
	return total_area

def trapezoid (n, a, b, f):
	total_area=0
	width = (b-a)/n
	while (a<b):
		if (f==1):
			height=(f1(a)+f1(a+width))/2
		elif(f==2):
			height=(f2(a)+f2(a+width))/2
		elif(f==3):
			height=(f3(a)+f3(a+width))/2
		elif(f==4):
			height=(f4(a)+f4(a+width))/2
		elif(f==5):
			height=(f5(a)+f5(a+width))/2
		area = height*width
		total_area=total_area+area
		a+=width
	return total_area
	
	
def main():
	again=1
	while (again ==1):
		print ("Function 1: 5x^4+3x^3-10x+2")
		print ("Function 2: x^2-10")
		print ("Function 3: 40x+5")
		print ("Function 4: x^3")
		print ("Function 5: 20x^2+10x-2")
		function = int(input("Enter Function: "))
		print ("Find area with rectangles or trapezoids?")
		method = int(input("Enter 1 for rectangles, 2 for trapezoids, 3 for both, 4 to quit: "))
		if (method==1):
			n = int(input("Enter number of intervals: "))
			a = int(input("Enter Starting Point: "))
			b = int(input("Enter Ending Point: "))
			print ("Starting point: ",(a))
			print ("Ending point: ",(b))
			print ("Number of intervals: ",(n))
			print ("Area: ",(rectangle(n, a, b, function)))
			print ("Use again?")
			again = int(input("Press 1 to use again, Press 0 to quit"))
		elif (method==2):		
			n = int(input("Enter number of intervals: "))
			a = int(input("Enter Starting Point: "))
			b = int(input("Enter Ending Point: "))	
			print ("Starting point: ",(a))
			print ("Ending point: ",(b))
			print ("Number of intervals: ",(n))
			print ("Area: ",(trapezoid(n, a, b, function)))		
			print ("Use again?")
			again = int(input("Press 1 to use again, Press 0 to quit"))
		elif (method==3):
			n = int(input("Enter number of intervals: "))
			a = int(input("Enter Starting Point: "))
			b = int(input("Enter Ending Point: "))
			print ("Rectangular Area: ",(rectangle(n, a, b, function)))
			print ("Trapezoidal Area: ",(trapezoid(n, a, b, function)))
			print ("Use again?")
			again = int(input("Press 1 to use again, Press 0 to quit"))
		else:
			print ("Quit")
			again=0


main()





