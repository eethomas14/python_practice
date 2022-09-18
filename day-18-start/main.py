import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

tim = Turtle()

def rand_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_tuple = (red, green, blue)
    return color_tuple

def draw_figure(sides):
    angle = 360 / sides
    tim.pencolor(rand_color())
    for _ in range(sides):
        tim.fd(50)
        tim.right(angle)

i = 3

while i <= 10:
    draw_figure(i)
    i += 1

screen = Screen()
screen.exitonclick()
