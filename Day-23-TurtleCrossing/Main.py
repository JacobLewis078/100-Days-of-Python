import time
from turtle import Screen
from cars import Cars
from Turtles import Turtles
from levelboard import Levelboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.bgcolor("white")

leo = Turtles()
level = Levelboard()
car = Cars()


screen.listen()
screen.onkey(leo.go_forward, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_cars()
    screen.update()
    level.level_up(leo, car)

    for cars in car.all_cars:
        if cars.distance(leo) < 25:
            level.game_over()
            game_is_on = False

if screen.onkey(level.restart_game, "r"):
    game_is_on = True

screen.exitonclick()
