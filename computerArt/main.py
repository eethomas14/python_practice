import turtle
import random
turtle.colormode(255)
turt = turtle.Turtle()
turt.penup()
turt.hideturtle()
color_list = [(250, 248, 245), (251, 248, 249), (198, 163, 116), (131, 79, 51), (224, 211, 115), (239, 243, 246), (246, 249, 246), (82, 39, 28), (116, 40, 30), (170, 153, 27), (55, 86, 122), (71, 114, 78), (123, 156, 177), (176, 103, 97), (129, 148, 137), (44, 52, 63), (39, 34, 41), (49, 53, 52), (221, 180, 182), (217, 182, 177), (76, 72, 47), (185, 149, 151), (187, 208, 171), (115, 138, 122), (103, 78, 80), (96, 124, 161), (175, 191, 212), (90, 48, 49), (165, 109, 110), (58, 62, 71)]

turt.setheading(225)
turt.forward(380)
turt.setheading(0)
turt.speed("fastest")
num_dots = 100

for dot_count in range(1, num_dots + 1):
    turt.dot(20, random.choice(color_list))
    turt.fd(50)

    if dot_count % 10 == 0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)

screen = turtle.Screen()
screen.exitonclick()