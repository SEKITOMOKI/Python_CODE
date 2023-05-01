from turtle import *
setup(600,400)

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
write("LOVE YOU",align="center",font=("Arial",20,"bold"))
done()#也可使用mainloop()保持画布不消失，直到手动关闭