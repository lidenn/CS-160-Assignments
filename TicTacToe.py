#Program:Tic Tac Toe
#Author: Dennis Li
#Date: 10/26/16
#Description: This program allows two users to play Tic Tac Toe
#Input:User character choice, and location for Tic Tac Toe
#output:The Winner of the game and the score during all of the rounds


#Function:print_board
#Description:This prints out the array that was created
#Parameters:3x3 Array
#Pre-conditions:A 3 by 3 array is entered for the score
#Post-conditions:Displays the 3 by 3 array 
#Return:None
def print_board(board):
	for r in range(3):
		for c in range (3):
			print (board[r][c] + '|', end="")
		print()
		print("------")


#Function: example
#Description: Displays the example board for the user input
#Parameteres: None
#Pre-conditions: None
#Post-conditions: Display of the example board
#Return:None
def example():
	num=0
	example =[[num]*3,[num]*3,[num]*3]
	for r in range(3):
		for c in range (3):
			example[r][c]=num
			print (example[r][c],'|', end="")
			num+=1
		print()
		print("--------")


#Function:place_x
#Description:Places an x into the array depending on the user input
#Parameters:An array
#Pre-conditions: A 3x3 array for the scoreboard
#Post-conditions:An index in the 3x3 array filled with an X
#Return: None
def place_x(board):
	example()
	valid=False
	while (valid==False):
		box = int(input("Enter box number: "))
		if (box==0 and board[0][0]==' '):
			board[0][0]='x'
			valid = True
		elif (box==1 and board[0][1]==' '):
			board[0][1]='x'
			valid = True
		elif (box==2 and board[0][2]==' '):
			board[0][2]='x'
			valid = True
		elif (box==3 and board[1][0]==' '):
			board[1][0]='x'
			valid = True
		elif (box==4 and board[1][1]==' '):
			board[1][1]='x'
			valid = True
		elif (box==5 and board[1][2]==' '):
			board[1][2]='x'
			valid = True
		elif (box==6 and board[2][0]==' '):
			board[2][0]='x'
			valid = True
		elif (box==7 and board[2][1]==' '):
			board[2][1]='x'
			valid = True
		elif (box==8 and board[2][2]==' '):
			board[2][2]='x'
			valid = True
		elif (box>8 or box<0):
			print ("Enter between 0-8")
		else:
			print ("Box already filled, enter new box")

#Function:place_o
#Description:Places an o into the array depending on the user input
#Parameters:An array
#Pre-conditions: A 3x3 array for the scoreboard
#Post-conditions:An index in the 3x3 array filled with an O
#Return: None


def place_o(board):
	example()
	valid=False
	while (valid==False):
		box = int(input("Enter box number: "))
		if (box==0 and board[0][0]==' '):
			board[0][0]='o'
			valid = True

		elif (box==1 and board[0][1]==' '):
			board[0][1]='o'
			valid = True
		elif (box==2 and board[0][2]==' '):
			board[0][2]='o'
			valid = True
		elif (box==3 and board[1][0]==' '):
			board[1][0]='o'
			valid = True
		elif (box==4 and board[1][1]==' '):
			board[1][1]='o'
			valid = True
		elif (box==5 and board[1][2]==' '):
			board[1][2]='o'
			valid = True
		elif (box==6 and board[2][0]==' '):
			board[2][0]='o'
			valid = True
		elif (box==7 and board[2][1]==' '):
			board[2][1]='o'
			valid = True
		elif (box==8 and board[2][2]==' '):
			board[2][2]='o'
			valid = True
		elif (box>8 or box<0):
			print ("Enter between 0-8")
		else:
			print ("Box already filled, enter new box")

#Function:check_x
#Description:checks to see if there are 3 x's in a row
#Parameters: An array 
#Pre-conditions A 3 by 3 array with some of the indexes filled
#Post-conditions: Returns 1 if there is 3 in a row
#Return:Returns a 1, which is used to keep score
def check_x(board):
	if(board[0][0]=='x' and board[0][1]=='x' and board[0][2]=='x'):
		return 1
	if(board[1][0]=='x' and board[1][1]=='x' and board[1][2]=='x'):
		return 1
	if(board[2][0]=='x' and board[2][1]=='x' and board[2][2]=='x'):
		return 1
	if(board[0][0]=='x' and board[1][0]=='x' and board[2][0]=='x'):
		return 1
	if(board[0][1]=='x' and board[1][1]=='x' and board[2][1]=='x'):
		return 1
	if(board[0][2]=='x' and board[1][2]=='x' and board[2][2]=='x'):
		return 1
	if(board[0][0]=='x' and board[1][1]=='x' and board[2][2]=='x'):
		return 1
	if(board[0][2]=='x' and board[1][1]=='x' and board[2][0]=='x'):
		return 1

#Function:check_o
#Description:checks to see if there are 3 o's in a row
#Parameters: An array 
#Pre-conditions A 3 by 3 array with some of the indexes filled
#Post-conditions: Returns 1 if there is 3 in a row
#Return:Returns a 1, which is used to keep score


def check_o(board):
	if(board[0][0]=='o' and board[0][1]=='o' and board[0][2]=='o'):
		return 1
	if(board[1][0]=='o' and board[1][1]=='o' and board[1][2]=='o'):
		return 1
	if(board[2][0]=='o' and board[2][1]=='o' and board[2][2]=='o'):
		return 1
	if(board[0][0]=='o' and board[1][0]=='o' and board[2][0]=='o'):
		return 1
	if(board[0][1]=='o' and board[1][1]=='o' and board[2][1]=='o'):
		return 1
	if(board[0][2]=='o' and board[1][2]=='o' and board[2][2]=='o'):
		return 1
	if(board[0][0]=='o' and board[1][1]=='o' and board[2][2]=='o'):
		return 1
	if(board[0][2]=='o' and board[1][1]=='o' and board[2][0]=='o'):
		return 1



#Function: player_is_x
#Description: If player 1 is x, it will run the game with the first choice as x
#Parameters: An array
#Pre-conditions: A 3 by 3 array for the game board
#Post-conditions A filled 3 by 3 game board
#Return: Returns 1 if player 1 win, return 2 if player 2 wins
def player_is_x(board):
	place_x(board)				
	print_board(board)		
	for turn in range (4):
		place_o(board)
		print_board(board)		
		if (check_o(board)==1):
			print("Player 2 Wins")
			return 2

		place_x(board)
		print_board(board)			
		if (check_x(board)==1):	
			print("Player 1 Wins")
			return 1
	return 3

#Function: player_is_o
#Description: If player 1 is o, it will run the game with the first choice as o
#Parameters: An array
#Pre-conditions: A 3 by 3 array for the game board
#Post-conditions A filled 3 by 3 game board
#Return: Returns 1 if player 1 win, return 2 if player 2 wins
def player_is_o(board):
	place_o(board)
	print_board(board)		
	for turn in range (4):
		place_x(board)
		print_board(board)		
		if (check_x(board)==1):
			print("Player 2 Wins")
			return 2 
		place_o(board)
		print_board(board)
		if (check_o(board)==1):	
			print("Player 1 Wins")
			return 1
	return 3
		

#Function:main
#Description:Run the entire game and give the option for the users to play again
#Parameters:None
#Pre-conditions: 2 players
#Post-conditions: Shows the score for the two players
#Return: None

def main():
	turn =0
	player1_score=0
	player2_score=0
	tie=0
	again = True
	while (again==True):	
		board =[[' ']*3,[' ']*3,[' ']*3]
		valid_choice=False
		while (valid_choice==False):
			X_or_O = str(input("Player 1 pick X or O: "))

			if (X_or_O == 'x' or X_or_O == 'X'):
				valid_choice=True
				game=player_is_x(board)
				if (game==1):
					player1_score+=1
				elif (game==2):
					player2_score+=1
				elif (game==3):
					tie+=1
		
				print ("player 1 score: ", player1_score)
				print ("player 2 score: ", player2_score)
				print ("Ties: ", tie)
		
			elif (X_or_O == 'O' or X_or_O == 'o'):
				valid_choice=True
				game = player_is_o(board)
				if (game==1):
					player1_score+=1
				elif (game==2):
					player2_score+=1
				elif (game==3):
					tie+=1
	
				print ("player 1 score: ", player1_score)
				print ("player 2 score: ", player2_score)
				print ("Ties: ", tie)

			else:
				print("Input: X or O")

		print("Play again?")
		turn=int(input("Enter 1 to play again, or Enter 2 to stop: "))
		if (turn==1):
			again=True
		if (turn==2):
			again=False





main();
