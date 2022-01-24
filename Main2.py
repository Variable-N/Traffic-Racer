from Car import car
from Road import Road
from turtle import *
import random
import winsound
#FPS limiter
from FPS import *

#Function:

#Functions

def playerSpeed(speed):
    r0.speedY(speed)
    r1.speedY(speed)
    r2.speedY(speed)
    r3.speedY(speed)
    r4.speedY(speed)
    r5.speedY(speed)


def newRoad(r):
    if r.roadmark1.ycor() < -750:
        r.setRoad(750)

def newCar(c):
    if c.carBody.ycor() + 80 < -500:
        c.GoTo(c.carBody.xcor(),580+random.randint(0,30)*10)
    #Random color cars
        r = random.randint(0,10)/10
        g = random.randint(0,10)/10
        b = random.randint(0,10)/10
        c.carBody.color(r,g,b)
        if r - 0.1 < 0: r = 0.1
        if g - 0.1 < 0: g = 0.1
        if b - 0.1 < 0: b = 0.1
        c.carRoof.color(r-0.1,g-0.1,b-0.1)
    #Random speed
        c.speedY = random.randint(20,50)/10


def playerLeft():
    if playercar.carBody.xcor() == -400:
        return
    playercar.GoTo(playercar.carBody.xcor()-40,-250)

def playerRight():
    if playercar.carBody.xcor() == 400:
        return
    playercar.GoTo(playercar.carBody.xcor()+40,-250)

def opponentSpeed(spd):
    op0.RunY(spd)
    op1.RunY(spd)
    op2.RunY(spd)
    op3.RunY(spd)
    op4.RunY(spd)


#PLayer collide with other card
def collision():
    for opX in oppoCarsArray:
        if playercar.carBody.xcor() + 41 > opX.carBody.xcor() -41 and  playercar.carBody.xcor() - 41 < opX.carBody.xcor() +41 :
            if playercar.carBody.ycor() + 80 > opX.carBody.ycor() -80 and  playercar.carBody.ycor() - 80 < opX.carBody.ycor() +80 :
                return True
    return False


def scoreUpdate(inc):
    global score
    for opX in oppoCarsArray:
        if playercar.carBody.ycor()  <= inc + opX.carBody.ycor() and playercar.carBody.ycor() + inc >= opX.carBody.ycor():
            score += 1
            pen.clear()
            pen.write("SCORE: {}".format(score),align = "center", font=("Arial",24,"normal", 'bold'))


#Main Menu


#in game function:
def Run():
    global plySpeed, difficultyIncrease
    increment = 3
    while True:
        if score %25 == 0 and difficultyIncrease and score != 0:
            plySpeed += 3
            increment += 0.5
            difficultyIncrease = False
        if not difficultyIncrease and not score %25 == 0:
            difficultyIncrease = True
        
        fps = FPS()
        fps.fpsLimit(120)
        opponentSpeed((plySpeed/2)*-1)
        playerSpeed(plySpeed)
        for i in range(len(roadsArray)):
            newRoad(roadsArray[i])
        for i in range(len(oppoCarsArray)):
            newCar(oppoCarsArray[i])
        scoreUpdate(increment)
        if collision():
            window.clear()
            break
        window.update()

def MainMenu():
    win = Screen()
    win.title("Car test")
    win.bgcolor(0,0,0.2)
    pe = Turtle()
    pe.speed(0)
    pe.color("white")
    pe.hideturtle()
    pe.goto(0,0)
    pe.write("BEST RACING GAME xD",align = "center", font=("Arial",30,"normal", 'bold'))
    pe.penup()
    
    
    
x = 0
#Main Loop
while True:
    fp = FPS()
    window = Screen()
    window.title("Car test")
    window.bgcolor(0,0,0.2)
    #window.bgpic("BG1.gif")

    window.setup(width=1000,height=1000)
    window.tracer(0)


    #Road Mark
    r0 = Road()
    r0.setRoad(-500)
    r1 = Road()
    r1.setRoad(-250)
    r2 = Road()
    r2.setRoad(0)
    r3 = Road()
    r3.setRoad(250)
    r4 = Road()
    r4.setRoad(500)
    r5 = Road()
    r5.setRoad(750)




    # Player car

    playercar = car(0,0.5,0)
    playercar.GoTo(0,-250)

    # Opponent car 
    yArray = [700, 400,-250, 200, -40]
    op0 = car(0,1,1)
    op0.GoTo(-400,yArray[random.randint(0,4)])
    op1 = car(0.8,0.8,0.8)
    op1.GoTo(-200,yArray[random.randint(0,4)])
    op2 = car(1,0.5,0.5)
    op2.GoTo(0,yArray[random.randint(0,4)])
    op3 = car(0.5,0.5,1)
    op3.GoTo(200,yArray[random.randint(0,4)])
    op4 = car(1,1,0)
    op4.GoTo(400,yArray[random.randint(0,4)])




    window.listen()
    window.onkeypress(playerLeft, "a")
    window.onkeypress(playerRight, "d")

    #ARRAYS
    roadsArray = [r0,r1,r2,r3,r4,r5]
    oppoCarsArray = [op0,op1,op2,op3,op4]

    # Border


    borderL = Turtle()
    borderL.speed(0)
    borderL.shape("square")
    borderL.color("red")
    borderL.shapesize(stretch_wid=51, stretch_len= 1)
    borderL.penup()
    borderL.goto(-500,0)

    borderR = Turtle()
    borderR.speed(0)
    borderR.shape("square")
    borderR.color("red")
    borderR.shapesize(stretch_wid=51, stretch_len= 1)
    borderR.penup()
    borderR.goto(500,0)

    borderU = Turtle()
    borderU.speed(0)
    borderU.shape("square")
    borderU.color("red")
    borderU.shapesize(stretch_wid=1, stretch_len= 51)
    borderU.penup()
    borderU.goto(0,505)

    borderD = Turtle()
    borderD.speed(0)
    borderD.shape("square")
    borderD.color("red")
    borderD.shapesize(stretch_wid=1, stretch_len= 51)
    borderD.penup()
    borderD.goto(0,-500)



    # Score System
    score = 0        

    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,400)
    pen.write("SCORE: {}".format(score),align = "center", font=("Arial",24,"normal", 'bold'))
    difficultyIncrease = True
    plySpeed = 10
    winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
    Run()
    window.clear()
    print("Your score is: ",score)
    