from turtle import Turtle,Screen
STARTING_POSITION=(0 , -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)


    def go_up(self):
        new_y=self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

    def go_left(self):
        new_x=self.xcor() - 20
        self.goto(new_x,self.ycor())

    def go_right(self):
        new_x=self.xcor() + 20
        self.goto(new_x,self.ycor())

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor()>295:
            return True
        else:
            return False