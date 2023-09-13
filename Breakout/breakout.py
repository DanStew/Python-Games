import turtle

#Creating the window
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=500,height=600)
wn.title("Breakout")

#Creating the paddle
paddle = turtle.Turtle()
paddle.penup()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1,stretch_len=4)
paddle.goto(0,-200)
paddle.dx = 8

#Creating the ball
ball = turtle.Turtle()
ball.penup()
ball.shape("square")
ball.speed(0)
ball.color("white")
ball.goto(0,0)
ball.dx = 4
ball.dy = 4

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
        self.speed = 10
        self.coords = coords

        #Setting up the cubes turtle
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.color("red")
        self.turtle.shape("square")
        self.turtle.goto(coords)

#Creating the cubes
redCube_1 = RedCube((20,280))
cubes = []
cubes.append(redCube_1)
print(cubes[0].coords)

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
        ball.sety(-280)
        ball.dy *= -1

    #Checking for ball collision with paddle
    if (ball.ycor() < -190 and ball.ycor() > -210 and (ball.xcor() < paddle.xcor() + 40 and ball.xcor() > paddle.xcor() -40)):
        ball.dy *= -1
        ball.sety(-190)

    #Checking to see if the ball 
    for cube in cubes:
        if ((ball.xcor() < cube.coords[0] + 20 and ball.xcor() > cube.coords[0] -20) and (ball.ycor() < cube.coords[1] + 20 and ball.ycor() > cube.coords[1] -20)):
            cube.turtle.hideturtle()