# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# Redone @Justin Orr

import turtle # basic graphics, and very simple games

win = turtle.Screen() # the window for the game, IMPORTANT: (0,0) is in the center of the screen!
win.title("Pong by @TokyoEdTech")
win.bgcolor("black")
win.setup(width = 800, height = 600) #set the size of the window
win.tracer(0) # stop the window from updating, we will manually update in order to speed up the game significantly

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation, NOT the movement speed of the paddle
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup() # turtles draw lines as they move, so this stops that
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup() 
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup() 
ball.goto(0, 0)

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
win.listen() # listen for keyboard input
win.onkeypress(paddle_a_up, "w") # call paddle_a_up when w is pressed, note that w is lower case so capital w will not work
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update() # every loop around, update the screen, this is similar to how it is done in unity