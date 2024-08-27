from turtle import *
import random

setup(800, 800)

# tiling: xlocation ylocation sizeOfScreen levelofRecursion => draw
def tiling(x, y, size, level):
    #reach final level of recursion
    if level == 0:
        if random.random() < 0.5:
            #vertical line
            penup()
            goto(x,y - size)
            pendown()
            goto(x,y + size)
        else:
            #horizontal line
            penup()
            goto(x - size, y)
            pendown()
            goto(x + size, y)
    else: #split screen and go to next level of recursion
        #reduce size by half
        size /= 2
        level -= 1
        tiling(x - size, y + size, size, level)
        tiling(x + size, y + size, size, level)
        tiling(x - size, y - size, size, level)
        tiling(x + size, y - size, size, level)
Screen().bgcolor("#AFCBFF") 
donatello = Turtle("turtle")
donatello.color("#AFCBFF")
donatello.pencolor("white")
hideturtle()
tiling(0,0,300,4)
tracer(True)
exitonclick()