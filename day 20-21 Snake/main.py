from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Update

screen= Screen()
screen.title("Snake Game")
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0)

snake= Snake()
food= Food()
score= Update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #DETECT collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    #Detect collision with wall
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() < -230 or snake.head.ycor() > 230:
        score.reset()
        snake.reset()
     
     #detect collisoin with tail
    for segment in snake.snake[1:]:
         if snake.head.distance(segment)< 15:
             score.reset()
             snake.reset()
     
screen.exitonclick()