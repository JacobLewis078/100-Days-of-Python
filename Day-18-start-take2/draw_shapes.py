from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
# Her method


def draw_shape(num_sides):
    angle = 360 / num_sides
    timmy.color(colors[num_sides - 3])
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

# my original method:
# for number in range(12):
#    if number >= 3:
#        degree = 360 / number
#        for _ in range(number):
#            timmy.forward(30)
#            timmy.right(degree)
#            timmy.forward(30)


screen = Screen()
screen.exitonclick()
