from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.penup()
        self.shapesize(.8, .8)
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

    def past_boundary(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        self.move()
