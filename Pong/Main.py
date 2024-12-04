import time
from turtle import Screen
from paddles import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle()
right_paddle = Paddle()
left_paddle.left_player()
right_paddle.right_player()
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(left_paddle.up, key="w")
screen.onkey(left_paddle.down, key="s")
screen.onkey(right_paddle.up, key="Up")
screen.onkey(right_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 325 or
        ball.distance(left_paddle) < 50 and ball.xcor() < -325):
        ball.bounce_x()

    # right paddle misses
    if ball.xcor() > 390:
        ball.past_boundary()
        scoreboard.increase_l_score()

    # left paddle misses
    if ball.xcor() < -390:
        ball.past_boundary()
        scoreboard.increase_r_score()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False

if scoreboard.l_score == 10 or scoreboard.r_score == 10:
    scoreboard.game_over()

screen.exitonclick()
