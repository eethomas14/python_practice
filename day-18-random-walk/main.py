import random
from turtle import Turtle, Screen

tim = Turtle()

colors = ["orange red", "magenta", "yellow", "green yellow", "deep pink", "deep sky blue", "blue violet", "dark green",
          "dark blue", "dark goldenrod"]

tim.pensize(5)
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.pencolor(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
