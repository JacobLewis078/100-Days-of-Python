from turtle import Turtle


class Levelboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.update_level()

    def update_level(self):
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.write(f"Level {self.current_level}", align="center", font=("Courier", 30, "normal"))

    def level_up(self, turtle, car):
        if turtle.ycor() > 280:
            self.clear()
            self.current_level += 1
            self.update_level()
            turtle.start_of_level()
            car.increase_speed()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"Game Over! \nFinal Level: {self.current_level}", align="center", font=("Courier", 30, "normal"))

    def restart_game(self):
        self.goto(0, -250)
        self.write("Press Space to restart game", align="center", font=("Courier", 24, "normal"))
        return True
