# import colorgram

# colors = colorgram.extract('image.jpg', 20)
#
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_list.append(new_color)
#
# print(colors)
# print(color_list)

import turtle
from turtle import Turtle, Screen
import random

color_to_paint = [(211, 155, 105), (64, 93, 144), (150, 73, 56), (140, 163, 195), (231, 204, 125), (137, 77, 100), (139, 185, 156), (200, 133, 147), (218, 77, 56), (57, 131, 101), (78, 161, 99), (198, 90, 109), (156, 209, 190), (46, 37, 73), (119, 109, 161), (57, 52, 95)]

turtle.colormode(255)
leo = Turtle()
leo.hideturtle()
leo.penup()
y_position = -250
leo.setposition(-250, y_position)

for y in range(10):
    y += 50
    y_position += y
    leo.setposition(-250, y_position)
    for x in range(10):
        leo.dot(20, random.choice(color_to_paint))
        leo.forward(50)


screen = Screen()
screen.exitonclick()

