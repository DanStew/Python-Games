import pygame
import random


"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

#Initialising the pygame fonts so they can be used 
pygame.font.init()

# GLOBALS VARS
#Setting up the dimensions of the screen
s_width = 800
s_height = 700
#These are different variables as the play area doesnt take up the whole screen
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30

#Representing the top left x and y of the play area to be used
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS
#These shapes are made up of multiple lists to represent the multiple rotations that that shapes could have
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

#Creating a list to hold all of the shapes and then assigning a color to each of the shapes
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

#The main data strucutre for the game
#Representing the different pieces on the board
class Piece(object):
	def __unit__(self, x, y, shape):
		self.x = x
		self.y = y
		self.shape = shape
		#Shapes.index(shape) finds the index of the given shape in the shapes array
        #This is then used to find the correct color to assing the shape
		self.color = shape_colors[shapes.index(shape)]
		self.rotation = 0

#Creating the grid to be drawn onto the screen
def create_grid(locked_positions={}):
    #Creating a list of 10 colours (0,0,0) to represent the columns in a row
    #Then, creating 20 of these lists of 10 colors to represent the different rows in the grid
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
	
    #Looping through every item within the grid
    #Note : I don't know why it is j,i and then i,j
    for i in range(len(grid)):
        for j in range(len(grid[i])):
		#Seeing any item in the grid is in the locked position dictionary
            if (j,i) in locked_positions : 
		    #Finding and setting the color of that pixel
                colour = locked_positions[(j,i)]
                grid[i][j] = colour
	
    #Returning the grid
    return grid
	

def convert_shape_format(shape):
	pass

def valid_space(shape, grid):
      pass

def check_lost(positions):
	pass

def get_shape():
	#Returning a random shape from the shapes array
      #Makes this shape a piece so it can be used
	return Piece(5,0,random.choice(shapes))


def draw_text_middle(text, size, color, surface):
	pass

#Drawing the grid to the screen  
def draw_grid(surface, grid):
    #Drawing the individual boxes onto the screen
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #Drawing for a square for each space within the grid, assigned the color grid[i][j]
            #,0 means there is no border
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)
    
    #Drawing the play area border onto the screen
    pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)	

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface,grid):
    #Filling the screen to be black
    surface.fill((0,0,0))
	
    #Setting up the font to draw to the screen
    font = pygame.font.SysFont("comicsans",60)
    label = font.render("Tetris", 1, (255,255,255))
    surface.blit(label, (top_left_x + play_width/2 - label.get_width(), block_size)) #Blocksize can be changed to static if needed
    
    #Drawing the grid onto the screen
    draw_grid(surface,grid)

    pygame.display.update()	


def main(win):
      locked_positions = {}
      grid = create_grid(locked_positions)
      change_piece = False
      run = True
      current_piece = get_shape()
      next_piece = get_shape()
      clock = pygame.time.Clock()
      fall_time = 0

      while run:
            for event in pygame.event.get():
                  #Checking to see if the user wants to quit out
                  if event.type == pygame.QUIT:
                        run = False
            
                  #Checking to see if the user presses a key
                  #Then applying the correct move to the square
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                              current_piece.x -= 1
                              #Checking to see if the move is a valid move, and if not, reversing the move made
                              if not(valid_space(current_piece,grid)):
                                    current_piece.x += 1

                        if event.key == pygame.K_RIGHT:
                              current_piece.x += 1
                              #Checking to see if the move is a valid move, and if not, reversing the move made
                              if not(valid_space(current_piece,grid)):
                                    current_piece.x -= 1

                        if event.key == pygame.K_DOWN:
                              current_piece.x += 1
                              #Checking to see if the move is a valid move, and if not, reversing the move made
                              if not(valid_space(current_piece,grid)):
                                    current_piece.y -= 1

                        if event.key == pygame.K_UP:
                              current_piece.rotation += 1
                              #Checking to see if the move is a valid move, and if not, reversing the move made
                              if not(valid_space(current_piece,grid)):
                                    current_piece.rotation -= 1
            
            #Drawing the grid onto the surface
            draw_window(win,grid)


def main_menu(win):
	main(win)

#Making the window
win = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Tetris")

main_menu(win)  # start game