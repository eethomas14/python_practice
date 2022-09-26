from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "orange"]

y_positions = [-60, -20, -0, 20, 40]
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which tutle will win the race? Please enter a color: ")
race = False
turt_list = []

for i in range(0, 5):
    turt = Turtle(shape="turtle")
    turt.color(colors[i])
    turt.penup()
    turt.goto(x=-230, y=y_positions[i])
    turt_list.append(turt)

if user_bet:
    race = True

while race:
    for turt in turt_list:
        if turt.xcor() > 210:
            race = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"The winning turtle is {winning_color}. You win!")
            else:
                print(f"The winning turtle is {winning_color}. You lose!")

        rand_dist = random.randint(0, 10)
        turt.forward(rand_dist)

screen.exitonclick()
