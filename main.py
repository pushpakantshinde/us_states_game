import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"       # Only .gif image be added in turtle

screen.addshape(image)              # It adds new shape to the existing types of shape e.g circle, square, ....

#turtle = turtle.Turtle

turtle.shape(image)

# #-----------------------------------------------------------------------------------------------------------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# # We want the coordinates for all states by clicking on it and then prepare the data file but in our case all data is
# # already given in '50_states.csv' file
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()           # keep the screen open even after clicking on it
# #-----------------------------------------------------------------------------------------------------------------------


# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
# answer_state_capital = answer_state.title()
# print(answer_state_capital)


title = "Guess the State"

state_data = pandas.read_csv("50_states.csv")     # Dataframe
states = state_data["state"]
states_list = states.to_list()

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()

score = 0
shall_continue = True

while shall_continue:

    answer_state = screen.textinput(title=title, prompt="What's another state's name?")
    answer_state_capital = answer_state.title()

    if answer_state_capital == "Exit":
        # Create '.csv' file which will contain the names of states that user could not guess
        x_list = []
        y_list = []

        missing_states_list = states_list

        for state in missing_states_list:
            state_details = state_data[state_data["state"] == state]
            x_list.append(int(state_details.x))
            y_list.append(int(state_details.y))

        data_dict = {
            "state": states_list,
            "x": x_list,
            "y": y_list
        }

        dataframe = pandas.DataFrame(data_dict)
        dataframe.to_csv("states_to_learn.csv")

        break

    if answer_state_capital in states_list:
        state_details = state_data[state_data["state"] == answer_state_capital]
        x_cor = int(state_details.x)                    # state_details.x is stored as 'string',so need to convert it into 'int'
        y_cor = int(state_details.y)                    # state_details.y is stored as 'string',so need to convert it into 'int'
        my_turtle.goto(x_cor, y_cor)
        my_turtle.write(arg=f"{answer_state_capital}", align="center", font=("Arial", 8, "normal"))
        score += 1
        states_list.remove(answer_state_capital)        # remove the item to avoid repeatation if the same state name is entered again

        title = f"{score}/50 States Correct"

        if score == 50:
            shall_continue = False

#screen.exitonclick()