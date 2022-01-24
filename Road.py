from turtle import *
class Road:
    def __init__(self):
        # Road mark 1
        self.roadmark1 = Turtle()
        self.roadmark1.speed(0)
        self.roadmark1.shape("square")
        self.roadmark1.color("white")
        self.roadmark1.shapesize(stretch_wid=7, stretch_len= 0.5)
        self.roadmark1.penup()
        
        # Road mark 2
        self.roadmark2 = Turtle()
        self.roadmark2.speed(0)
        self.roadmark2.shape("square")
        self.roadmark2.color("white")
        self.roadmark2.shapesize(stretch_wid=7, stretch_len= 0.5)
        self.roadmark2.penup()
        
        # Road mark 3
        self.roadmark3 = Turtle()
        self.roadmark3.speed(0)
        self.roadmark3.shape("square")
        self.roadmark3.color("white")
        self.roadmark3.shapesize(stretch_wid=7, stretch_len= 0.5)
        self.roadmark3.penup()
        
        # Road mark 4
        self.roadmark4 = Turtle()
        self.roadmark4.speed(0)
        self.roadmark4.shape("square")
        self.roadmark4.color("white")
        self.roadmark4.shapesize(stretch_wid=7, stretch_len= 0.5)
        self.roadmark4.penup()

    def setRoad(self,r1):
        self.roadmark1.goto(-300,r1)
        self.roadmark2.goto(-100,r1)
        self.roadmark3.goto(100,r1)
        self.roadmark4.goto(300,r1)

    def speedY(self,speed):
        self.roadmark1.sety(self.roadmark1.ycor()-speed)
        self.roadmark2.sety(self.roadmark2.ycor()-speed)
        self.roadmark3.sety(self.roadmark3.ycor()-speed)
        self.roadmark4.sety(self.roadmark4.ycor()-speed)
