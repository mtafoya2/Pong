from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#create screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

screen.tracer(0)

#Create a paddle class
right_paddle = Paddle(x_pos = 350, y_pos = 0)
left_paddle = Paddle(x_pos= -350, y_pos= 0)

#Create a ball class
ball = Ball()

#Create a scoreboard
scoreboard = Scoreboard()

#listen for keystrokes
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

is_running = True
while is_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision with top/bottom wall
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce_y()

    #Detect collision with right paddle 
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    

screen.exitonclick()