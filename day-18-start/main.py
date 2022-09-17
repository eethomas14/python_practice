from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("magenta3")

for _ in range(4):
    timmy_the_turtle.fd(50)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()