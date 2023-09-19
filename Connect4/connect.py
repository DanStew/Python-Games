import pygame
import numpy as np
import sys
import math

#Defining colours to be used
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

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

#Functions below are to make the gui for the game
def draw_board(board):
    board = np.flip(board,0)
    #Looping through every circle in the grid
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            #Making a rectangle and then drawing a circle over them for each piece
            pygame.draw.rect(screen, BLUE, (col*SQUARESIZE,row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))

            #Finding the correct color to draw the circle
            if board[row][col] == 0 : color = BLACK
            if board[row][col] == 1 : color = RED 
            if board[row][col] == 2 : color = YELLOW
            #Drawing the circle onto the grid
            pygame.draw.circle(screen, color, (int(col*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)



#Terminal state check
game_over = False

#Making the board
board = create_board()

#Defining who's turn it is
turn = 0

#Initialising pygame
pygame.init()
#Defining and Making the screen size
SQUARESIZE = 100
radius = (int(SQUARESIZE) / 2 - 5)
width = COLUMN_COUNT*SQUARESIZE
height = (ROW_COUNT + 1) *SQUARESIZE # +1 included to include top row to place counters
size = (width,height)
screen = pygame.display.set_mode(size)
draw_board(board)

#Initialising a font to be used to write
myFont = pygame.font.SysFont("monospace", 75)

#Main game function
while not game_over:

    #Updating the display
    pygame.display.update()

    #Processing all of the events that pygame takes in
    #This event loop is what is needed to ensure the pygame window remains open
    for event in pygame.event.get():

        #Allowing the user to exit the game
        if event.type == pygame.QUIT:
            sys.exit()

        #Checking to see where the users mouse it
        if event.type == pygame.MOUSEMOTION:
            #Blacking out previous circles draw
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            #Drawing the circle onto the screen
            if turn % 2 == 0: pygame.draw.circle(screen, RED, (event.pos[0], int(SQUARESIZE/2)), radius)
            else : pygame.draw.circle(screen, YELLOW, (event.pos[0], int(SQUARESIZE/2)), radius)
    
        #Seeing if the user wants to drop a piece
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Asking for players inputs
            if turn % 2 == 0:
                #event.pos[0] returns the x position where the user has pressed
                col = int(math.floor(event.pos[0] / SQUARESIZE))
                player = 1  
            else:
                col = int(math.floor(event.pos[0] / SQUARESIZE))
                player = 2
    
            #Making the move the player submitted
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board,row,col,player)
                validMove = True

                #Printing the board to the screen
                draw_board(board)

                #Checking to see whether the user has won
                if winning_move(board,player):
                    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                    label = myFont.render("Player 1 wins!!", 1, RED)
                    screen.blit(label, (20,20))
                    pygame.time.wait(3000)
                    game_over = True

                #Incrementing the turn variable
                turn += 1
            #Error Handling if move is invalid
            else : 
                print("Invalid Move, Go again")
                break
            

    

    