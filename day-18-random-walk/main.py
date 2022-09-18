import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)

def rand_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_tuple = (red, green, blue)
    return color_tuple

tim.pensize(5)
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.pencolor(rand_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
