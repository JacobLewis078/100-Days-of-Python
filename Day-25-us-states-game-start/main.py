import turtle
import pandas

correctly_guessed = 0

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#     turtle.onscreenclick(get_mouse_click_coor)
state_data = pandas.read_csv("50_states.csv")
state_names = state_data.state
print(state_names)

while correctly_guessed < 50:
    screen.title(f"U.S. States Game: Correctly Guessed {correctly_guessed}/50")
    answer_state = screen.textinput("Guess the States", "What's another state's name?")
    answer_state = answer_state.title()
    for state in state_names:
        if answer_state == state:
            correctly_guessed += 1
            answer = state_data[state_data.state == answer_state]
            x = int(answer.x)
            y = int(answer.y)
            answer_text = turtle.Turtle()
            answer_text.penup()
            answer_text.hideturtle()
            answer_text.goto(x, y)
            answer_text.write(f"{state}")

turtle.write("You Got all 50 States! Way to Go!", align="center", font=("Courier", 40, "bold"))



turtle.mainloop()
