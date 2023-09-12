from turtle import Turtle

STARTING_POSITIONS=[(0,0), (-20, 0), (-40,0)]
DISTANCE= 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head = self.snake[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.snake[0].color("yellow")
        
    def add_segment(self, position):
            snake_body=Turtle("square")
            snake_body.color("purple")
            snake_body.penup()
            snake_body.goto(position)
            self.snake.append(snake_body)

    def extend(self):
        self.add_segment(self.snake[-1].position())
            
    def move(self): 
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_x= self.snake[seg_num-1].xcor()
            new_y= self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(DISTANCE)
        
    def up(self):
        if self.snake[0].heading()!=DOWN:
            self.snake[0].setheading(UP)
        
    def down(self):
        if self.snake[0].heading()!=UP:    
            self.snake[0].setheading(DOWN)
        
    def left(self):
        if self.snake[0].heading()!=RIGHT:
            self.snake[0].setheading(LEFT)
        
    def right(self):
        if self.snake[0].heading()!=LEFT:
            self.snake[0].setheading(RIGHT)
            
    def reset(self):
        for seg in self.snake:
            seg.hideturtle()
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]