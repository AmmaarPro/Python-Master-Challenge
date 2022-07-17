import math
import turtle

for i in range(12):
    t = math.sin(i * 30)
    print(i * 30, t)


wn = turtle.Screen()
T = turtle.Turtle()
sc = turtle.Screen()
sc.reset()

sc.setworldcoordinates(0, -1.5, 1800, 1.5)


T.pencolor('red')
for angle in range(1800):
    T.pendown()
    y = math.sin(math.radians(angle))
    T.goto(angle, y)

T.pencolor("blue")
T.penup()

x = math.cos(math.radians(angle))
T.goto(angle, x)

for angle in range(1800):
    T.pendown()
    x = math.cos(math.radians(angle))
    T.goto(angle,x)

wn.exitonclick()