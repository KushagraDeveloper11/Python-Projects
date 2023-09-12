# import colorgram

# colors= colorgram.extract('image.jpg', 5)
# print(colors)

import turtle as t
from turtle import Turtle, Screen
import random

squirtle= Turtle()
squirtle.shape("turtle")
squirtle.color("deep sky blue")
squirtle.penup()
t.colormode(255)
squirtle.speed(0)
squirtle.hideturtle()

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return (r,g,b)

squirtle.setheading(225)
squirtle.forward(300)
squirtle.setheading(0)

for i in range(1, 101):
    color= random_color()
    squirtle.dot(20, color)
    squirtle.forward(50)
    
    if i%10==0:
        squirtle.setheading(90)
        squirtle.forward(50)
        squirtle.setheading(180)
        squirtle.forward(500)
        squirtle.setheading(0)

screen= t.Screen()
screen.exitonclick()