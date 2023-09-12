from turtle import Turtle, Screen

squirtle= Turtle()
screen= Screen()

# def move_forward():
#     squirtle.fd(10)

# screen.listen()
# screen.onkey(key="space", fun= move_forward)

def move_forward():
    squirtle.forward(10)
def move_backward():
    squirtle.backward(10)    
def anticlockwise():
    squirtle.left(45)
def clockwise():
    squirtle.right(45)
def clear_screen():
    squirtle.clear()  
    squirtle.penup()
    squirtle.home()
    squirtle.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()