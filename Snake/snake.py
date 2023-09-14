import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows=20
    w=500

    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        
    def move(self, dirnx, dirny):
        #Setting the new values for the direction of the cube
        self.dirnx = dirnx
        self.dirny = dirny
        #Updating the cubes position
        self.pos = (self.pos[0]+ self.dirnx, self.pos[1] + self.dirny)
        
    def draw(self, surface, eyes=False):
        #Finding the distance between x and y values
        dis = self.w // self.rows

        #Finding the i and j of the position you want to draw
        #This is where in the rows and columns, not the pixel count
        i = self.pos[0]
        j = self.pos[1]

        #Drawing a rectangle for the cube
        #The +1 and -1 in the coordinates are needed so you can still see the lines of the grid
        #Otherwise, the cube would be drawn over the grid lines
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-1,dis-1))

        #Drawing the eyes onto the cube if head
        if eyes : 
            #This is the math that is needed to position the circles correctly
            centre = dis//2
            radius = 3
            #This is the math finding the coordinates of the centre of the circles
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis-radius*2, j*dis+8)
            #This is the code to draw the circles onto the window
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)



#This is the object that makes the snake
#The snake object is made up of cube objects
class snake(object):
    #Making a list of all of the cubes that the snake is made up of
    snakeBody = []
    turns = {}

    #Initialising the snake object
    def __init__(self,color,pos):
        self.color = color
        #Initialising the head of the snake at it given position
        self.head = cube(pos)
        #Adding the head cube to the list of cubes
        self.snakeBody.append(self.head)
        #Setting the initial values for the direction of the snake
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        #Looping through all of the possible events that pygame collects
        for event in pygame.event.get():
            #Seeing if the user has pressed the red x
            if event.type == pygame.QUIT:
                #Closing the application
                #This is the first event that you want to program in your games
                #Otherwise, when the user tries to close out of your game, it won't work
                pygame.quit()
            
            #Collecting all of the key values that the user has pressed
            #This returns a list/dictionaries of all keys, along with a 0 or 1 on whether they have been pressed
            keys = pygame.key.get_pressed()

            #Looping through all keys and seeing if they are pressed
            for key in keys : 
                #This checks to see whether any of the important keys have been pressed (are 1)
                #If so, the if statement will be true and will run the code
                #Elifs have been used so users can't move in more than 1 direction at once
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    #Changing the direction of the snake
                    self.dirnx = -1
                    self.dirny = 0

                    #Rememebering where you turned
                    #Adding a key to the turns dictionary of the current position of the head of the snake
                    #At this key, the direction that you turned, dirnx and dirny has been stored
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    #Changing the direction of the snake
                    self.dirnx = 1
                    self.dirny = 0

                    #Remembering where you turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    #Changing the direction of the snake
                    self.dirnx = 0
                    self.dirny = -1

                    #Remembering where you turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    #Changing the direction of the snake
                    self.dirnx = 0
                    self.dirny = 1

                    #Remembering where you turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        #Moving the cubes
        for i,cube in enumerate(self.snakeBody):
            #Finding the position of the cube in the body
            p = cube.pos[:]
            #Checking to see if the head turned at that position
            if p in self.turns:
                #Creating an array of the way that the snake turned
                turn = self.turns[p]
                #Turning the snake in the correct direction
                cube.move(turn[0],turn[1])
                #Checks to see if the current cube is the last cube in the snake's body
                if i == len(self.snakeBody) -1:
                    #If so, the turn is popped as it no longer needed
                    #This is needed as it allows the user to be able to turn at that position again
                    #If this wasn't included, whenever you go this square, you will automatically turn
                    self.turns.pop(p)
            #Moving the cube if the snake hasn't turned
            else : 
                #First 4 are edge checking the snake
                #This occurs when the snake goes off the screen and then appears at the other side
                if cube.dirnx == -1 and cube.pos[0] <= 0: cube.pos = (cube.rows-1, cube.pos[1])
                elif cube.dirnx == 1 and cube.pos[0] >= cube.rows-1: cube.pos = (0, cube.pos[1])
                elif cube.dirny == 1 and cube.pos[1] >= cube.rows-1: cube.pos = (cube.pos[0], 0)
                elif cube.dirny == -1 and cube.pos[1] <= 0: cube.pos = (cube.pos[0], cube.rows-1)
                #This is the line of code that will normally be run 
                else: cube.move(cube.dirnx, cube.dirny)

    #Resetting the snake and all of its information
    #This is so that the game restarts
    def reset(self,pos):
        print("Snake has been reset")
        self.head = cube(pos)
        self.snakeBody = []
        self.snakeBody.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        #Finding the tail of the snake (Last item in snakeBody list)
        tail = self.snakeBody[-1]
        dx,dy = tail.dirnx, tail.dirny

        #Positioning where the new cube will be placed (and also creating the cube)
        if dx == 1 and dy == 0:
            self.snakeBody.append(cube((tail.pos[0] -1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.snakeBody.append(cube((tail.pos[0] +1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.snakeBody.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.snakeBody.append(cube((tail.pos[0],tail.pos[1]+1)))

        #Setting the direction of the new cube just made to be the same as the tail
        self.snakeBody[-1].dirnx = dx
        self.snakeBody[-1].dirny = dy

    #Drawing the snake
    def draw(self,surface):
        #Looking through every cube in the snake
        for i,cube in enumerate(self.snakeBody):
            #Checking to see whether the snake if the first cube in the snake or not
            #This is done as the head is slightly different to the others (has eyes)
            if i ==0:
                cube.draw(surface,True)
            else:
                cube.draw(surface)

#Drawing the grid onto the window
def drawGrid(w,rows,surface):
    #Defining how big each square in the grid is
    sizeBtwn = w // rows #// is integer divide is python

    #Initialing x and y
    x = 0
    y = 0

    #Drawing the lines onto the window
    for line in range(rows):
        #Updating the new values of x and y to be drawn
        x += sizeBtwn
        y += sizeBtwn

        #Drawing the lines onto the grid
        #Syntax (surface, linecolour, start point, endpoint)
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

#Updating the window
def redrawWindow(surface):
    #Making these variables global
    global rows, width, s, snack
    #Filling the screen black
    surface.fill((0,0,0)) 
    #Drawing the grid onto the screen
    drawGrid(width,rows,surface)
    #Drawing the snake
    s.draw(surface)
    #Drawing the snack
    snack.draw(surface)
    #Updating
    pygame.display.update() 

def randomSnack(rows,item):
    positions = item.snakeBody
    while True : 
        x = random.randrange(rows)
        y = random.randrange(rows)
        #This line of code ensures that the new x,y position generated isn't already taken by the snake
        #Could not use this line by filtering through all positions of snake cubes and checking to see if any are equal to the x,y generated
        #This complex line just simplifies the issue
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            #This repeats until a unique value for x and y are generated
            continue
        else : 
            break
    return (x,y)

#Creating a message box to show that the user has lost
def message_box(subject,content):
    #Creating a new window to show the message
    root = tk.Tk()
    #This ensures that this new window appears above everything else
    root.attributes("-topmost", True)
    root.withdraw()
    #Showing the information given into the function
    messagebox.showinfo(subject,content)

    #Makes it so that the messagebox remains
    #It think this is because it keeps trying to destroy it but it can't
    try:
        root.destroy()
    except:
        pass
    

#This is the main function that everything is called from
def main():
    #Making key variables global
    global width, rows, s, snack

    #This is the dimensions of the window to be created
    #Only need 1 variable as grid is 500x500
    width = 500

    #Make sure that is divisable by the width and height
    rows = 20

    #Creating the window
    win = pygame.display.set_mode((width,width)) 

    #Creating the snake for the game
    s = snake((255,0,0), (10,10)) 

    #Creating the snake
    snack = cube(randomSnack(rows,s), color=(0,255,0))

    #Creating the clock to add delay
    clock = pygame.time.Clock()

    #Creating the mainloop for the game
    flag = True
    while flag:
        #Adding some delay to the game
        pygame.time.delay(50) 
        #Ensures game doesn't run more than 10fps
        clock.tick(6) 

        #Moving the snake
        s.move()

        #Checking to see whether the head of the snack is at the snacks positions
        if s.snakeBody[0].pos == snack.pos:
            #Adding a cube to the snack
            s.addCube()
            #Making a new snack
            snack = cube(randomSnack(rows,s), color=(0,255,0))
        
        #Checking to see if the snake has killed itself
        #Looping through all of the cubes in the body
        for x in range(len(s.snakeBody)):
            #Seeing if any of the cubes have the same position
            if s.snakeBody[x].pos in list(map(lambda z:z.pos, s.snakeBody[x+1:])):
                print("Score: ", len(s.snakeBody))
                message_box("You Lost!","Play Again...")
                s.reset((10,10))
                break

        #Redrawing the window
        redrawWindow(win)
        

main()