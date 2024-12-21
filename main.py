from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter the color: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
i = -100
race_turtles = []
race_on = False

for color in colours:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=i)
    i += 30
    race_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtles in race_turtles:
        if 230 < turtles.xcor():
            race_on = False
            winning_color = turtles.pencolor()
            if user_bet == turtles.pencolor():
                print(f"You won. {winning_color} turtle won the race.")
            else:
                print(f"You lost. {winning_color} turtle won the race.")
        turtles.forward(random.randint(0, 10))

screen.exitonclick()
