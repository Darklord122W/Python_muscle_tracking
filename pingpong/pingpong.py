from turtle import Screen,Turtle

myscreen=Screen()
myscreen.bgcolor("black")
myscreen.setup(width=800,height=600)

t=Turtle()
t.hideturtle()
t.color("white")
# Draw the square
t.penup()
t.goto(350,0)
t.begin_fill()
t.setheading(90)   # up (north)
t.forward(50)
t.setheading(0)   # right
t.forward(20)
t.setheading(270)   # down
t.forward(100)
t.setheading(180)   # left
t.forward(20)
t.setheading(90)   # up
t.forward(50)
t.end_fill()



myscreen.exitonclick()
