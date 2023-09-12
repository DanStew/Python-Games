import turtle

#Creating the window for the game
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)

#This command stops the window from updating
#This means that you have to update the window yourself
#This for some reason speeds up the game, not sure
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
#This line sets the speed of animation, this sets the speed to the maximum possible speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
#This line of code changes the shape of the object
#The default size is 20x20, this code stretches the width by 5 and length by 1
#So the new size is 100x20, as 20x5 is 100
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
#Penup is used as by default these objects draw a line behind them, as they move
#You don't want this, so penup is used
paddle_a.penup()
#This is how you set the starting location of an object
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
#The lines of code below means that, every time the ball moves, it moves by x amount of pixels
ball.dx = 0.1
ball.dy = 0.1

#Moving the paddles

#Paddle moving functions
def paddle_a_up():
    #Finding the y coordinate of the paddle
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    #Finding the y coordinate of the paddle
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
#This code tells the wn to listen for when a button is pressed on the keyboard
wn.listen()
#This code then calls the correct function in response to what has been pressed
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
#Below is hwo you use the Up and Down arrows when listening
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Initialising player score and text
player1_score = 0
player2_score = 0

#Creating a Pen to draw the text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
#Means that you won't see the pen actually move
pen.hideturtle()
pen.goto(0,260)
#Writing the score of the game to the screen
pen.write(f"Player A: {player1_score} Player B: {player2_score}", align="center", font=("Courier",24))

#Main game loop
while True:
    #Every time the window runs, it updates the screen
    wn.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    #This checks to see whether the ball has met the border and then resets the direction of the ball
    if ball.ycor() >= 290:
        ball.sety(290)
        #This reverse the directions that the ball is going
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    #These 2 below check to see whether the player has scored
    if ball.xcor() >= 390:
        player1_score += 1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {player1_score} Player B: {player2_score}", align="center", font=("Courier",24))

    if ball.xcor() <= -390:
        player2_score += 1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {player1_score} Player B: {player2_score}", align="center", font=("Courier",24))

    #Checking to see whether the ball has hit a paddel
    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50)):
        ball.dx *= -1
        ball.setx(-340)

    #Checking to see whether the ball has hit a paddel
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50)):
        ball.dx *= -1
        ball.setx(340)
