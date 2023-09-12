from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars= []
        self.car_speed= STARTING_MOVE_DISTANCE
        
    def generate_cars(self):
        random_chance= random.randint(1,6)
        if random_chance==1:
            car=Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            random_y= random.randint(-240, 240)
            car.goto(300, random_y)
            self.all_cars.append(car)
        
    def move_car(self):
        for cars in self.all_cars:
            new_x= cars.xcor()- self.car_speed
            cars.goto(new_x, cars.ycor())
            
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
