from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
is_race_on = False
colors = ["red", "blue", "yellow", "green", "orange", "purple"]
y_position = -80
turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position)
    y_position += 30
    turtles.append(new_turtle)

user_bet = screen.textinput(title="What is your bet?", prompt="What color turtle do you predict will win the race?: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You are correct! {winning_turtle} won!")
            else:
                print(f"You were wrong! {winning_turtle} won!")

    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
# leo = Turtle(shape="turtle")
# leo.penup()
# leo.color("blue")
# leo.goto(-230, -80)
#
# donny = Turtle(shape="turtle")
# donny.penup()
# donny.color("purple")
# donny.goto(-230, -50)
#
# mikey = Turtle(shape="turtle")
# mikey.penup()
# mikey.color("orange")
# mikey.goto(-230, -20)
#
# ralphy = Turtle(shape="turtle")
# ralphy.penup()
# ralphy.color("red")
# ralphy.goto(-230, 10)
#
# splinter = Turtle(shape="turtle")
# splinter.penup()
# splinter.color("yellow")
# splinter.goto(-230, 40)
#
# shredder = Turtle(shape="turtle")
# shredder.penup()
# shredder.color("green")
# shredder.goto(-230, 70)

screen.exitonclick()

