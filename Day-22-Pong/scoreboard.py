from turtle import Turtle
from ball import Ball


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def increase_l_score(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.l_score == 10:
            self.goto(0, 0)
            self.write("Left Player Wins!", align="center", font=("Courier", 40, "normal"))
        if self.r_score == 10:
            self.goto(0, 0)
            self.write("Right Player Wins!", align="center", font=("Courier", 40, "normal"))

