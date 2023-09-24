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
	def __init__(self, x, y, shape):
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
	
#Converting the shape lists into its actual format to be used in the game
def convert_shape_format(shape):
    #Generating the lists of positions where the blocks are
    positions = []
    #Finding the correct format that the shape is in given the rotation that it has
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
          #Makes it easier to adapt the line by making it a list
          row = list(line)
          for j,column in enumerate(row):
                #Checking to see if the current item is a block (0)
                if column == '0':
                      #Adding the position of each block in the shape into the positions array
                      positions.append((shape.x+j, shape.y+i))
      
    for i, pos in enumerate(positions):
          #Giving each position in the positions array an offset
          #This moves everything to the left and up
          #This is so that, when displaying it, it is more accurate to the screen
          positions[i] = (pos[0] -2, pos[1] -4)
          
    return positions

def valid_space(shape, grid):
      #Making a list of all spaces on the grid
      #The if means that you only add it into the accepted positions if the space is empty
      #This is because you can't put a grid in a spot that is taken already
      accepted_pos = [[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
      #Converting this list into 1 dimension
      #Turning every item in the list above and overwriting them into a 1 dimensional list
      accepted_pos = [j for sub in accepted_pos for j in sub]

      """
      To visualise what the code above has just done, it has converted the list to what can be seen below : 
      [ [(1,1)] , [(2,1)], ...] --> [ (1,1), (2,1), ...]
      This makes it a lot easier to loop through as each item is a tuple, rather than an individual array with a tuple inside
      """

      #Taking the given shape and converting it into positions
      formatted = convert_shape_format(shape)

      #Checking to see whether all of the positions in the formatted shape is within the accepted positions
      #This works as image if you trying to move off the edge of the screen
      #This pixel won't be part of the accepted positions and therefore the move will be rejected
      for pos in formatted:
            if pos not in accepted_pos:
                  #Only asking if it is in a valid position if the y value is > -1
                  #Not off the screen
                  if pos[1] > -1:
                        return False
      return True

#Checking if any of the positions are above the screen
#This means you are above the screen and have lost
def check_lost(positions):
      for pos in positions : 
            x,y = pos
            if y < 1: 
                  return True
      return False

def get_shape():
	#Returning a random shape from the shapes array
      #Makes this shape a piece so it can be used
	return Piece(5,0,random.choice(shapes))

#Drawing any text to the middle of the screen
def draw_text_middle(text, size, color, surface):
      font = pygame.font.SysFont("comicsans", size, bold=True)
      label = font.render(text,1,color)
      surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - (label.get_height()/2)))

#Drawing the grid to the screen  
def draw_grid(surface, grid):
    #Drawing the horizontal and vertical lines onto the screen
    for i in range(len(grid)):
          pygame.draw.line(surface, (128,128,128), (top_left_x, top_left_y + i*block_size), (top_left_x+play_width, top_left_y + i*block_size))
          for j in range(len(grid[i])):
              pygame.draw.line(surface, (128,128,128), (top_left_x + j*block_size,top_left_y), (top_left_x + j*block_size, top_left_y+play_height))    
                
#To clear the row a row has been has been completed
def clear_rows(grid, locked):
    #Incremental variable
    #This variable helps to understand how many rows you have to shift down
    inc = 0
    #Looping through all of the rows in the table
    for i in range(len(grid)-1, -1,-1):
          row = grid[i]
          #Seeing if the color black is not in the row
          #If it isn't, it means that the row is full and needs to be deleted
          if (0,0,0) not in row:
                inc += 1
                ind = i 
                #Looping through every place within the row and deleted it from locked positions
                for j in range(len(row)):
                      try:
                            del locked[(j,i)]
                      except:
                            continue
     
    #Code to shift every other row down
    #When deleting from the array, the row deleted is essentially removed from memory
    #This means that, rather than having to shift everything down, you instead have to add a row at the top of the list
    if inc > 0:
          #The key loops through every item in the locked positions list
          #The key = lambda... sorts the lockedpositions list by its y value, to group all of the y values together
          # [::-1] makes it so that the list is looked at backwards
          #It is looked at backwards so that you don't overwrite existing rows
          #If you looked at it from the top to the bottom, as you move down the rows, previous rows will be overwritten
          for key in sorted(list(locked), key = lambda x:x[1])[::-1]:
              x,y = key
              #Seeing if the y value is above the index of the row that you removed
              if y < ind:
                    #Making the new positons for the key to shift it down
                    newKey = (x,y+inc)
                    #Making a new key in locked with the same color value as the previous key did
                    #locked.pop returns the color of the cube
                    locked[newKey] = locked.pop(key)   
    return inc         

#Drawing the next shape off the screen, and showing what it is
def draw_next_shape(shape, surface):
    #Drawing some text to the screen
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255,255,255))

    #Defining some positioning variables (to help position the screen)
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 90

    #Getting the sublist of the shape that you want to draw
    format = shape.shape[shape.rotation % len(shape.shape)]

    #Drawing the blocks depending on where they show up in the list
    for i, line in enumerate(format):
          row = list(line)
          for j, column in enumerate(row):
                if column == '0' : 
                      pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)
    
    #Drawing the font to the screen
    surface.blit(label, (sx+10, sy-30))

def draw_window(surface,grid,score=0,highscore=0):
    #Filling the screen to be black
    surface.fill((0,0,0))

    #Drawing the score to the screen
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Score: " + str(score), 1, (255,255,255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    surface.blit(label, (sx+10, sy-100))

    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Highscore: " + str(highscore), 1, (255,255,255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    surface.blit(label, (sx-10, sy-200))

    #Setting up the font to draw to the screen
    font = pygame.font.SysFont("comicsans",60)
    label = font.render("Tetris", 1, (255,255,255))
    surface.blit(label, (top_left_x + play_width/2 - label.get_width() + 80, block_size - 10)) #Blocksize can be changed to static if needed
    
    #Drawing the individual boxes onto the screen
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #Drawing for a square for each space within the grid, assigned the color grid[i][j]
            #,0 means there is no border
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    #Drawing the play area border onto the screen
    pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)
    
    #Drawing the lines of the grid onto the screen
    draw_grid(surface,grid)

#Code to score the highscore for the game in the system
def update_score(nscore):
      score = max_score()
      
      with open('score.txt', 'w') as f:
            if int(score) > nscore:
                  f.write(str(score))
            else:
                  f.write(str(nscore))

#Getting the highscore from the textfile
def max_score():
      with open('score.txt', 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()
      return score


def main(win):
      #Initialising main variables in the program
      locked_positions = {}
      grid = create_grid(locked_positions)
      change_piece = False
      run = True
      current_piece = get_shape()
      next_piece = get_shape()
      clock = pygame.time.Clock()
      fall_time = 0
      fall_speed = 0.27
      level_time = 0
      score = 0

      #Finding the previous highscore
      highscore = max_score()

      while run:
            #Updating the new grid
            grid = create_grid(locked_positions)

            #This code means that blocks fall at the same time on all systems
            #This doesn't happen when you use fps
            fall_time += clock.get_rawtime() #Rawtime gets the until the last clock.tick()
            level_time += clock.get_rawtime()
            clock.tick()

            if level_time/1000 > 10:
                  level_time = 0
                  fall_speed *= 1.02
                  if fall_speed > 0.75:
                        fall_speed = 0.75

            #Checking to see if enough time has passed for the block to need to fall
            if fall_time / 1000 > fall_speed:
                  fall_time = 0
                  #Adding 1 to y value, moving it down the screen
                  current_piece.y += 1
                  #Ensuring the move is a valid move
                  if not(valid_space(current_piece,grid)) and current_piece.y>0:
                        #Reversing the move and changing the piece
                        current_piece.y -= 1
                        change_piece = True

            for event in pygame.event.get():
                  #Checking to see if the user wants to quit out
                  if event.type == pygame.QUIT:
                        run = False
                        pygame.display.quit()
            
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
                              current_piece.y += 1
                              #Checking to see if the move is a valid move, and if not, reversing the move made
                              if not(valid_space(current_piece,grid)):
                                    current_piece.y -= 1

                        if event.key == pygame.K_UP:
                              current_piece.rotation += 1
                              #Checking to see if the move is a valid move, and if not, reversing the move made
                              if not(valid_space(current_piece,grid)):
                                    current_piece.rotation -= 1
            
            #Finding the positions of the current piece your using
            shape_pos = convert_shape_format(current_piece)

            #Drawing the piece to the grid
            for i in range(len(shape_pos)):
                  x,y = shape_pos[i]
                  if y>-1:
                        grid[y][x] = current_piece.color

            #Checking to see if the piece needs to be changed
            if change_piece:
                  #Adding the color of the piece to the locked_positions dictionary
                  for pos in shape_pos:
                        p = (pos[0],pos[1])
                        locked_positions[p] = current_piece.color
                        #The format of the locked_positions dictioanry is : {(1,2) : (255,0,0), (2,1) : (255,0,0)}
                        #This is where the first item is the coordinate, and the second is the color that needs to be drawn there

                  #Updating the new piece
                  current_piece = next_piece
                  next_piece = get_shape()
                  change_piece = False
                  #Clearing the rows
                  cleared = clear_rows(grid, locked_positions)
                  score += 10*cleared

            #Drawing the grid onto the surface
            draw_window(win,grid,score,highscore)
            draw_next_shape(next_piece, win)
            pygame.display.update()

            #Checking to see if the user has lost
            if check_lost(locked_positions):
                  draw_text_middle("You Lost!", 60, (255,0,0), win)
                  pygame.display.update()
                  pygame.time.delay(1500)
                  update_score(score)
                  return
            

def main_menu(win):
      run = True
      while run:
            win.fill((0,0,0))
            draw_text_middle("Press any key to play", 60, (255,255,255), win)
            pygame.display.update()
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        run = False
                  if event.type == pygame.KEYDOWN:
                        main(win)
                  
	

#Making the window
win = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Tetris")

main_menu(win)  # start game