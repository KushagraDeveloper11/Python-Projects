from turtle import Turtle
ALIGN="center"
FONT=("Arial", 16, "normal")

class Update(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Day 15+\day 20-21 Snake\data.txt") as data:
            self.high_score= int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 225)
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)
        
        
    def increase_score(self):
        self.score+=1
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over.", align=ALIGN, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score=0
        self.update_score()