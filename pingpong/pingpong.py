from turtle import Screen,Turtle
from paddleclass import Paddle
from ballclass import Ball
import time
from scoreboard import Scoreboard


# t=Turtle()
# t.hideturtle()
# t.color("white")
# # Draw the square
# t.penup()
# t.goto(350,0)
# t.begin_fill()
# t.setheading(90)   # up (north)
# t.forward(50)
# t.setheading(0)   # right
# t.forward(20)
# t.setheading(270)   # down
# t.forward(100)
# t.setheading(180)   # left
# t.forward(20)
# t.setheading(90)   # up
# t.forward(50)
# t.end_fill()


myscreen=Screen()
myscreen.bgcolor("black")
myscreen.setup(width=800,height=600)
if __name__=="__main__":
    myscreen = Screen()
    myscreen.bgcolor("black")
    myscreen.setup(width=800, height=600)
    myscreen.tracer(0)
    Rightp=Paddle(350)
    Leftp=Paddle(-350)
    aball=Ball()
    score=Scoreboard()
    myscreen.listen()
    myscreen.onkeypress(Rightp.go_up, "Up")     # Up arrow moves the right paddle up
    myscreen.onkeypress(Rightp.go_down, "Down") # Down arrow moves it down
    myscreen.onkeypress(Leftp.go_up, "w")     # Up arrow moves the right paddle up
    myscreen.onkeypress(Leftp.go_down, "s") # Down arrow moves it down
    game_on=True
    while game_on:
        myscreen.update()
        aball.move()
        if aball.ycor()>280 or aball.ycor()<-280:
            aball.bounce_y()
        if aball.distance(Rightp)<50 and aball.xcor()>320 or aball.distance(Leftp)<50 and aball.xcor()<-320:
            aball.bounce_x()

# right paddle misses
        if aball.xcor()>380:
            aball.reset_p()
            score.l_point()
            score.update_scoreboard()

# left paddle misses
        if aball.xcor()<-380:
            aball.reset_p()
            score.r_point()
            score.update_scoreboard()
        
    myscreen.exitonclick()
