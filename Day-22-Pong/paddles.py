from turtle import Turtle

LEFT_X = -350
RIGHT_X = 350


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 3)
        self.color("white")
        self.penup()
        self.shapesize(1, 5)
        self.setheading(90)

    def left_player(self):
        self.goto(LEFT_X, y=0)

    def right_player(self):
        self.goto(RIGHT_X, y=0)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

