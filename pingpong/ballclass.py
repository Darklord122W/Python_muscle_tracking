from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(visible=True)       # set up the Turtle part first
        self.shape("circle")
        self.color("white","red")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.ymove=1
        self.xmove=1
        # self.showturtle()

    def move(self):
        if -400<self.xcor()<400 and -300<self.ycor()<300:
            self.sety(self.ycor() + self.ymove)
            self.setx(self.xcor() + self.xmove)

    def speed_UP(self):
        self.ymove*=1.1
        self.xmove*=1.1
    def bounce_y(self):
        self.ymove*=-1

    def bounce_x(self):
        self.xmove*=-1
        self.speed_UP()
    
    def reset_p(self):
        self.goto(0,0)
        self.bounce_x()
        self.ymove=1
        self.xmove=1


    