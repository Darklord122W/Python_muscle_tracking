from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(visible=True)       # set up the Turtle part first
        self.shape("circle")
        self.color("white","red")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.goto(0, 0)
        # self.showturtle()

    def move(self):
        if -400<self.xcor()<400 and -300<self.ycor()<300:
            self.sety(self.ycor() + 0.02)
            self.setx(self.xcor() + 0.02)
