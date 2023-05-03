from turtle import *
def draw_face():
    penup()
    goto(-120,0)
    pendown()
    seth(-90)
    pencolor("black")
    pensize(4)
    fillcolor("gold")
    begin_fill()
    circle(130,360)
    end_fill()

def draw_mouth():
    penup()
    goto(-80,-10)
    pendown()
    seth(-90)
    pencolor("black")
    pensize(4)
    circle(90,180)

def eyes_white():
    penup()
    forward(60)
    pendown()
    pensize(20)
    pencolor("white")
    seth(155)
    circle(100,45)

    penup()
    seth(180)
    forward(40)
    seth(155)
    pendown()
    pensize(20)
    pencolor("white")
    seth(155)
    circle(100,45)

def eyes_black(X):
    penup()
    seth(0)
    forward(X)
    pendown()
    pensize(15)
    pencolor("black")
    circle(5,360)
    penup()
    forward(110)
    pendown()
    circle(5,360)
    penup()
    hideturtle()

def emoji(x):
    draw_face()
    draw_mouth()
    eyes_white()
    eyes_black(x)


import time
n=0
while n<10:
    tracer(0)
    emoji(6)
    update()
    time.sleep(0.5)
    tracer(0)
    emoji(60)
    update()
    time.sleep(0.5)
    n=n+1

done()