import turtle
import pandas

screen= turtle.Screen()
image= "Day 15+\Day 25 Sporcle\india3.gif"
screen.title("Indian Sporcle")
screen.setup(width=600, height=600)
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

answer= screen.textinput("Guess The State", prompt="What's other state's name?")

data= pandas.read_csv("Day 15+\Day 25 Sporcle\indian_states.csv")
states= data.state.to_list()

if answer in states:
    t= turtle.Turtle()
    state_data= data[data.state == answer]
    t.hideturtle()
    t.penup() 
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer)


# turtle.mainloop()
screen.exitonclick()