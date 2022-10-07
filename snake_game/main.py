from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

seg = Turtle()
seg.shape("square")
seg.color("white")

initial_pos = [(0,0), (-20,0), (-40,0)]

for position in initial_pos:
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.goto(position)

screen.exitonclick()
