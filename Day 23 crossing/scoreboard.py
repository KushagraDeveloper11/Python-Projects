from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.score=1
        self.write(f"Level: {self.score}", align= "center", font= FONT)

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Level: {self.score}", align= "center", font= FONT)
        
    def display(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font= FONT)