import turtle
import time 
k=turtle.Turtle()
list=["green","yellow","red","blue","pink","violet","purple","orange"]
wn=turtle.Screen()
wn.bgcolor("black")
k.speed(0)
k.begin_fill()
k.fillcolor("red")
k.shape("turtle")
for i in range(1,300):
    k.color(list[i%8])
    k.pensize(i/10)
    k.forward(i)
    k.left(65)
k.end_fill()
turtle.hideturtle()
time.sleep(10)


