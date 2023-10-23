import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"       # Only .gif image be added in turtle

screen.addshape(image)              # It adds new shape to the existing types of shape e.g circle, square, ....

#turtle = turtle.Turtle

turtle.shape(image)

title = "Guess the State"

state_data = pandas.read_csv("50_states.csv")     # Dataframe
states = state_data["state"]
states_list = states.to_list()

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()

score = 0
shall_continue = True
