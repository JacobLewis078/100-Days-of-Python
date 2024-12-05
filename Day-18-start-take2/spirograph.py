import turtle
from turtle import Turtle, Screen
import random

leo = Turtle()
turtle.colormode(255)
leo.shape("turtle")
# leo.pensize(10)
leo.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for n in range (0, 360):
    leo.setheading(n)
    leo.pencolor(random_color())
    leo.circle(100)





# My Method for drawing random
#for i in range(200):
#    leo.pencolor(random_color())
 #   steps = int(random.random() * 50)
  #  angle = int(random.random() * 360)
   # leo.right(angle)
    #leo.fd(steps)

# Teacher's example for drawing random
#for _ in range(200):
 #   leo.pencolor(random.choice(colors))
  #  leo.forward(30)
   # leo.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
