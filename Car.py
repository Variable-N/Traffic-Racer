from turtle import *

class car:
    def __init__(self,r = 1, g = 1, b = 0):
        #Car body
        self.carBody = Turtle()
        self.carBody.speed(0)
        self.carBody.shape("square")
        self.carBody.color(r,g,b)
        self.carBody.shapesize(stretch_wid=8, stretch_len= 4)
        self.carBody.penup()
        #Car glass
        self.carGlass = Turtle()
        self.carGlass.speed(0)
        self.carGlass.shape("square")
        self.carGlass.color("aqua")
        self.carGlass.shapesize(stretch_wid=5, stretch_len= 3.5)
        self.carGlass.penup()
        #Car roof
        if r - 0.1 < 0: r = 0.1
        if g - 0.1 < 0: g = 0.1
        if b - 0.1 < 0: b = 0.1
        self.carRoof = Turtle()
        self.carRoof.speed(0)
        self.carRoof.shape("square")
        self.carRoof.color(r-0.1,g-0.1,b-0.1)
        self.carRoof.shapesize(stretch_wid=3.5, stretch_len= 3.5)
        self.carRoof.penup()

        #car speed X and Y axis
        self.speedX = 0
        self.speedY = 0

    def GoTo(self,x,y):
        self.carBody.goto(x,y)
        self.carGlass.goto(x,y-4)
        self.carRoof.goto(x,y-10)

    def RunX(self,speed = None):
        if speed is None:
            speed = self.speedX
        else:
            self.speedX = speed
        self.GoTo(self.carBody.xcor()+self.speedX,self.carBody.ycor())

    def RunY(self,speed = None):
        if speed is None:
            speed = self.speedY
        else: 
            self.speedY = speed
        self.GoTo(self.carBody.xcor(),self.carBody.ycor() +self.speedY)


#Tester Code 

# window = Screen()
# window.title("Car test")
# window.bgcolor(0,0,0.2)

# window.setup(width=1000,height=1000)
# window.tracer(0)

# playercar = car(1,1,0)
# playercar.GoTo(0,0)
# playercar.speedY = 0.1
# while True:
#     playercar.RunY()
#     window.update()
