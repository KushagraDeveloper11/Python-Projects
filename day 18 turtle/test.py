import turtle as t
from turtle import Turtle, Screen
import random

squirtle= Turtle()
squirtle.shape("turtle")
squirtle.color("deep sky blue")
squirtle.pencolor("black")



#dotted line:

# for i in range(5):
#     squirtle.forward(10)
#     squirtle.penup()
#     squirtle.forward(10)
#     squirtle.pendown()


#polygons using turtle:

# colours=["purple", "indigo", "blue", "green", "yellow", "orange", "red", "black"]
# j=3
# k=0
# while j<=10:
#     squirtle.pencolor(colours[k])
#     for i in range(j):
#         squirtle.forward(100)
#         squirtle.right(int(360/j))
#     j+=1
#     k+=1

t.colormode(255)

#To draw any random figure using turtle

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return (r,g,b)
    
# directions=[0, 90, 180, 270]
# squirtle.pensize(5)
squirtle.speed(0)
# color=()
# def random_move():
#     color= random_color()
#     move= random.randint(1,100)
#     squirtle.forward(move)
#     squirtle.pencolor(color)
#     squirtle.setheading(random.choice(directions))

# for  i in range(random.randint(1,100)):
#     random_move()
def draw_spiral(size_of_gap):
    for i in range(int(360/size_of_gap)):
        squirtle.color(random_color())
        squirtle.circle(100)
        squirtle.setheading(squirtle.heading()+size_of_gap )
        
draw_spiral(5)
screen= t.Screen()
screen.exitonclick()