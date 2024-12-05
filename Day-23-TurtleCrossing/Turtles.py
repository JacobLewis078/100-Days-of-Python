from turtle import Turtle


class Turtles(Turtle):
    def __init__(self):
        super().__init__()
        self.start_of_level()

    def start_of_level(self):
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def go_forward(self):
        self.forward(10)
        if self.xcor() > -300:
            self.clear()
