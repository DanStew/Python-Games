import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows=0
    w=0

    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
        
    def move(slef, dirnx, dirny):
        pass
        
    def draw(self, surface, eyes=False):
        pass

#This is the object that makes the snake
#The snake object is made up of cube objects
class snake(object):
    def __init__(self,color,pos):
        pass

    def move(self):
        pass

    def reset(self,pos):
        pass

    def addCube(self):
        pass

    def draw(self,surface):
        pass

def drawGrid(w,rows,surface):
    pass

def redrawWindow(surface):
    global width, rows, height
    win.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
    pass

def randomSnack(rows,items):
    pass

def message_box(subject,content):
    pass

#This is the main function that everything is called from
def main():

    #Making some variables global
    global width, rows, height

    #Making the window
    width = 500
    height = 500
    rows = 20 #Make sure that the rows is divisable by the width and height
    win = pygame.display.set_mode((width,height))
    
    #Making the snake object
    s = snake((255,0,0), (10,10))

    #Making a clock
    #This restricts how many frames per second the game is able to run
    clock = pygame.time.Clock()

    #Making the main loop
    flag = True
    while flag:
        #Delaying the game slightly, so doesn't move too fast
        pygame.time.delay(50)
        #Ensuring game can't run faster than 10 fps
        clock.tick(10)
        #Redrawing the window
        redrawWindow(win)

main()