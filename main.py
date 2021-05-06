from turtle import Turtle, Screen
from paddle_1 import Paddle
from ball import Ball
import time
from score import Score
screen = Screen()
screen.title("Welcome to Pong Game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.listen()
screen.tracer(0)

paddle_1 = Paddle((350, 0))

paddle_2 = Paddle((-350, 0))

ball = Ball()
scoreboard = Score()

screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")

screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collsion wiyh wall
    if ball.ycor()> 280 or ball.ycor() < -280:
        ball.bounce_y()
# detect collision with paddles
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2)< 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9
    #     detect ball out of the edges
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

















screen.exitonclick()