import turtle
import time

#Creating the window
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=500,height=600)
wn.title("Breakout")
wn.tracer(0)

#Creating the paddle
paddle = turtle.Turtle()
paddle.penup()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1,stretch_len=4)
paddle.goto(0,-200)
paddle.dx = 16

#Creating the ball
ball = turtle.Turtle()
ball.penup()
ball.shape("square")
ball.speed(0)
ball.color("white")
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#Moving the paddle

#Making the move paddle functions
def paddle_right():
    x = paddle.xcor()
    x += paddle.dx
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= paddle.dx
    paddle.setx(x)

#Listening for the key press events on the window
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_right, "d")
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_left, "s")

#Creating the cubes to be hit
class RedCube():
    def __init__ (self, coords):
        #Initial Setup of the Cube
        self.score = 20
        self.speed = 1.6
        self.coords = coords

        #Setting up the cubes turtle
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.color("red")
        self.turtle.shape("square")
        self.turtle.goto(coords)

class OrangeCube():
    def __init__ (self, coords):
        #Initial Setup of the Cube
        self.score = 15
        self.speed = 1.4
        self.coords = coords

        #Setting up the cubes turtle
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.color("orange")
        self.turtle.shape("square")
        self.turtle.goto(coords)

class YellowCube():
    def __init__ (self, coords):
        #Initial Setup of the Cube
        self.score = 10
        self.speed = 1.2
        self.coords = coords

        #Setting up the cubes turtle
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.color("yellow")
        self.turtle.shape("square")
        self.turtle.goto(coords)

class GreenCube():
    def __init__ (self, coords):
        #Initial Setup of the Cube
        self.score = 5
        self.speed = 0.6
        self.coords = coords

        #Setting up the cubes turtle
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.color("green")
        self.turtle.shape("square")
        self.turtle.goto(coords)

#Creating the cubes
cubes =[]
x = -220
for cube in range(12):
    #Creating 1 of each type of cube 10 times
    cubes.append(RedCube((x,260)))
    cubes.append(OrangeCube((x,220)))
    cubes.append(YellowCube((x,180)))
    cubes.append(GreenCube((x,140)))
    
    #Incrementing the x total
    x += 40

#Initialising score, lives and text
score = 0
lives = 3

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
#Means that you won't see the pen actually move
pen.hideturtle()
#Writing the score of the game to the screen
pen.goto(-220,-280)
pen.write(f"Score : {score}", align="left", font=("Courier",24))
pen.goto(40,-280)
pen.write(f"Lives : {lives}", align="left", font=("Courier",24))

#Making the gameover screen function
def gameOverScreen():
    wn.clear()
    wn.bgcolor("black")
    pen.goto(0,0)
    pen.write("Game Over ! ", align="center", font=("Courier", 32))

#Making the gamewin screen function
def gameWin():
    wn.clear()
    wn.bgcolor("black")
    pen.goto(0,0)
    pen.write("You Won ! ", align="center", font=("Courier", 32))

#Initialising the time part of this
lastTime = 0 

#Main loop for the game
while True : 
    wn.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Checking paddle wall collision
    if (paddle.xcor() < -210):
        paddle.setx(-210)

    if (paddle.xcor() > 210):
        paddle.setx(210)

    #Checking ball for wall collision
    if (ball.xcor() < -230):
        ball.setx(-230)
        ball.dx *= -1

    if (ball.xcor() > 230):
        ball.setx(230)
        ball.dx *= -1

    if (ball.ycor() > 280):
        ball.sety(280)
        ball.dy *= -1
    
    if (ball.ycor() < -280):
        #Setting procedure for if user dies
        #Updating the text
        lives -= 1
        pen.clear()
        pen.goto(-220,-280)
        pen.write(f"Score : {score}", align="left", font=("Courier",24))
        pen.goto(40,-280)
        pen.write(f"Lives : {lives}", align="left", font=("Courier",24))

        #Resetting speed and position
        ball.goto(0,0)
        ball.dx = 1
        ball.dy = 1
        time.sleep(1)

        #Checking GameOver
        if lives == -1:
            gameOverScreen()


    #Checking for ball collision with paddle
    if (ball.ycor() < -190 and ball.ycor() > -210 and (ball.xcor() < paddle.xcor() + 40 and ball.xcor() > paddle.xcor() -40)):
        ball.dy *= -1
        ball.sety(-190)

    #Checking to see if the ball 
    #First if is to reduce the amount of times this code has to be run
    #Time stuff introduced to stop multiple blocks being hit at the same time
    if (ball.ycor() > 120) and (time.time() - lastTime > 1): 
        for cube in cubes:
            if ((ball.xcor() < cube.coords[0] + 20 and ball.xcor() > cube.coords[0] -20) and (ball.ycor() < cube.coords[1] + 20 and ball.ycor() > cube.coords[1] -20)):
                #Hiding the cube so it can't be seen
                cube.turtle.hideturtle()
                #Popping the cube from the coords, so it is no longer checked
                cubes.remove(cube)
                #Setting the balls new speed
                ball.dy = -cube.speed

                #Updating the score
                score += cube.score
                pen.clear()
                pen.goto(-220,-280)
                pen.write(f"Score : {score}", align="left", font=("Courier",24))
                pen.goto(40,-280)
                pen.write(f"Lives : {lives}", align="left", font=("Courier",24))

                #Adding the time to delay this function
                lastTime = time.time()

        #Checking game win function
        if len(cubes) == 0:
            gameWin()
                
            