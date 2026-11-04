from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__(visible=True)       # set up the Turtle part first
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)
        # self.showturtle()

    def go_up(self):
        self.sety(self.ycor() + 20)

    def go_down(self):
        self.sety(self.ycor() - 20)