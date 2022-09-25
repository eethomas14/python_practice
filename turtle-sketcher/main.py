from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)

def move_backward():
    turt.backward(10)

def move_right():
    turt.right(10)

def move_left():
    turt.left(10)

def clear_screen():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()