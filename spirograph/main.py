import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)


tim.speed('fastest')

def rand_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_tuple = (red, green, blue)
    return color_tuple

def draw_circles(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(rand_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_circles(5)

screen = Screen()
screen.exitonclick()