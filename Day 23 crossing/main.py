import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

squirtle= Player()
score= Scoreboard()
car=CarManager()

screen.listen()
screen.onkey(squirtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_cars()
    car.move_car()
    
    #check if turtle touches finish_line
    if squirtle.ycor() == 280:
        squirtle.finish_line()
        score.update_score()
        car.increase_speed()
        
    #detect collision with car
    for i in car.all_cars:
        if i.distance(squirtle)<20:
            game_is_on=False
            score.display()

screen.exitonclick()