# no base case, no movement towards base case
"""
count = 1
while True:
    print(count)

"""

# it has base case but no movement towards bc

"""
count = 1
while True:
    if count > 10:
        break
    prin(count)

"""

# Base case and move towards 

"""
count = 1
while True:
    if count > 10:
        break
    count += 1

"""

# Python RTecursion = it has a base case + moce towards + recursive call

import turtle
from turtle import *

MAX_LENGTH = 500
INCREMENT = 20
#COLOR = "#3B5249"
COLOR = "green"

def draw_spiral(point_turtle, line_length):
    if line_length > MAX_LENGTH:
        return
    point_turtle.forward(line_length)
    point_turtle.right(90)
    draw_spiral(point_turtle, line_length + INCREMENT) #recursive call

Screen().bgcolor(COLOR) 
my_turtle = turtle.Turtle(shape="turtle")
my_turtle.pensize(5)
my_turtle.color('#BEC5AD')
draw_spiral(my_turtle,12)
turtle.done()

