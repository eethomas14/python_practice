# import turtle
# from turtle import *
#
# donatello = turtle.Turtle()
# print(donatello)
# donatello.shape("turtle")
# donatello.color("coral")
# donatello.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Acient Greek Philosophers",
["Parmenides","Plato","Aristotle"])
table.add_column("Acient Greek Poets",
["Homer","Aeschylus","Sophocles"])

table.align = "l"
print(table)