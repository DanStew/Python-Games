import pygame
import numpy as np

#Initialising board dimensions
#These variables are global, so capitalised
ROW_COUNT = 6
COLUMN_COUNT = 7

#Creating the board for the game, as a matrix
def create_board():
    #Creating a matrix for the board, filling all spaces with 0
    #A matrix is another word for a double array
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

#Function to drop a piece into the board
def drop_piece(board, row, col, piece):
     board[row][col] = piece
    

#Function to check location validity
def is_valid_location(board,col):
    #Checks to see whether the top row in the column is empty, if so returns true
    return board[ROW_COUNT-1][col] == 0

#Function to find next space in row
def get_next_open_row(board,col):
        #Looping through all rows in the grid
        for row in range(ROW_COUNT):
            #Returning the first instance where a space is 0
            if board[row][col] == 0:
                return row

#Checking to see whether any player has won
def winning_move(board,piece):
    #Checking for all horizal wins
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece : 
                return True
            
    #Checking for all vertical win locations
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece : 
                return True
    
    #Checking for positively sloped diagonals
    for col in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece : 
                return True

    #Checking for negatively sloped diagonals
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col-1] == piece and board[row+2][col-2] == piece and board[row+3][col-3] == piece : 
                return True       

#Function made to print the board in the conventional way
#This is because how the board is stored is in reverse to how we would usually visualise it
def print_board(board):
     #This command flips the matrix to be printed correctly
     print(np.flip(board,0))

#Terminal state check
game_over = False

#Making the board
board = create_board()

#Defining who's turn it is
turn = 0

#Main game function
while not game_over:
    #Printing the board to the screen
    print_board(board)

    #Asking for players inputs
    if turn % 2 == 0:
        col = int(input("Player 1, Make your Selection (0-6):"))
        player = 1  
    else:
        col = int(input("Player 2, Make your Selection (0-6):"))
        player = 2
    
    #Making the move the player submitted
    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board,row,col,player)
    
    #Checking to see whether the user has won
    if winning_move(board,player):
         print(f"Player {player} Wins!")
         break

    #Incrementing the turn variable
    turn += 1

    