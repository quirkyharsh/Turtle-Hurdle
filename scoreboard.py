from turtle import Turtle
FONT=("Courier",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-270,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"GAME OVER",align="center",font=FONT)



    def increase_level(self):
        self.level+=1
        self.update_scoreboard()