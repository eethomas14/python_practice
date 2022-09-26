from turtle import Turtle, Screen

colors = ["red", "green", "blue", "yellow", "orange"]

y_positions = [-40, -20, -0, 20, 40]
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which tutle will win the race? Please enter a color: ")

for i in range(0, 5):
    turt = Turtle(shape="turtle")
    turt.color(colors[i])
    turt.penup()
    turt.goto(x=230, y=y_positions[i])

screen.exitonclick()
