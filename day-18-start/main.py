import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

colors = ["orange red", "magenta", "yellow", "green yellow", "deep pink", "deep sky blue", "blue violet", "dark green",
          "dark blue", "dark goldenrod"]

def draw_figure(sides):
    angle = 360 / sides
    tim.pencolor(random.choice(colors))
    for _ in range(sides):
        tim.fd(50)
        tim.right(angle)

i = 3

while i < 10:
    draw_figure(i)
    i += 1

screen = Screen()
screen.exitonclick()
