from turtle import *
from time import sleep
setup(800,800)

#画爱心
pensize(5)
pencolor("red")

fillcolor("pink")
begin_fill()
left(135)
forward(100)

right(180)
circle(50,-180)

left(90)
circle(50,-180)

right(180)
forward(100)
right(135)
end_fill()

penup()
pencolor("black")
goto(0,80)
hideturtle()
pendown()
write("LOVE YOU",align="center",font=("Arial",20,"bold"))
sleep(1)
clear()

#画四叶草
penup()
pencolor("black")
pensize(5)
goto(0,0)
pendown()
for i in range(4):
    right(90)
    circle(50,180)
sleep(1)
clear()


#画红色五角星
penup()
pencolor("yellow")
pensize(5)
goto(-90,0)
pendown()
seth(0)
fillcolor("red")
begin_fill()
for i in range(5):
    forward(200)
    right(144)
end_fill()
sleep(1)
clear()

#画奥运五环
def getCircle(color):
    pendown()
    pencolor(color)
    circle(50,360)
    penup()
penup()
goto(0,0)
seth(0)
pensize(5)
goto(-80,0)
getCircle("blue")
goto(0,0)
getCircle("black")
goto(80,0)
getCircle("red")
goto(-40,-80)
getCircle("yellow")
goto(40,-80)
getCircle("green")
done()#也可使用mainloop()保持画布不消失，直到手动关闭