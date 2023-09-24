import pygame

#Making the window for the game
width = 500
height = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tutorial Networking")

#Variable to store the number of clients on the server
clientNumber = 0

#Setting up a class for a character
class Player():
    def __init__(self, x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.rect = (self.x,self.y,self.width,self.height)

def redraw_window(win,player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    player = Player(50,50,100,100,(0,255,0))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw_window(win,player)

main()