import turtle
import pandas

screen= turtle.Screen()
image= "Day 15+\Day 25 Sporcle\india3.gif"
screen.title("Indian Sporcle")
screen.setup(width=600, height=600)
screen.addshape(image)

turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)



data= pandas.read_csv("Day 15+\Day 25 Sporcle\indian_states.csv")
states= data.state.to_list()
guessed_states= []

while len(guessed_states) < 28:
    answer= screen.textinput(f"{len(guessed_states)}/28 are correct", prompt="What's other state's name?").title()
    if answer == "Exit":
    #     remaining_states=[]
    #     for i in states:
    #         if i not in guessed_states:
    #             remaining_states.append(i)
        remaining_states=[i for i in states if i not in guessed_states] 
        states_to_learn= pandas.DataFrame(remaining_states)
        states_to_learn.to_csv("Day 15+\Day 25 Sporcle\states_to_learn")
        break
    if answer in states:
        t= turtle.Turtle()
        state_data= data[data.state == answer]
        guessed_states.append(answer)
        t.hideturtle()
        t.penup() 
        t.pencolor("black")
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

# # turtle.mainloop()
# screen.exitonclick()
