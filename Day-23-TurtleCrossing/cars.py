from turtle import Turtle
import random

COLORS = ["blue", "green", "red", "yellow", "black", "pink", "orange", "purple"]
MOVE_INCREMENT = 5


class Cars:
    def __init__(self):
        super().__init__()
        self.starting_move_distance = 5
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 2:
            new_car = Turtle("square")
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT

