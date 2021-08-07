import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.screensize(800, 800)
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct", prompt="what the next states?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)

            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(answer_state)

not_guessed_state = [state for state in all_states if state not in guessed_state]
# for state in all_states:
#     if state not in guessed_state:
#         not_guessed_state.append(state)

if len(not_guessed_state)  == 0:
    pass
else:
    new_data = pandas.DataFrame(not_guessed_state)
    new_data.to_csv("missing_states.csv")

