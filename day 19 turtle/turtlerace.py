from turtle import Turtle,Screen
import random

screen= Screen()
screen.setup(width=1000, height=400)
user_bet= screen.textinput(title="Make your bet...", prompt="Which color will win the race?: ")
print(user_bet)
colors=["red", "orange", "yellow", "black", "green", "blue", "purple"]
y_position=[-150, -100, -50, 0, 50, 100, 150]
all_turtles= []

for turtle_index in range(0,7):
    new_turtle= Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-500, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>470:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle wins the race.")
            else:
                print(f"You've lost. The {winning_color} turtle wins the race.")
            
        rand_dist= random.randint(0,10)
        turtle.forward(rand_dist)
    

screen.exitonclick()