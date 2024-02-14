# Bryce Kelly
# COP 2500
# autopolygonator.py
# Oct 4, 2022
import turtle
sides = int(input("How Many Sides?\n"))
length = int(input("Total Length?\n"))
my_screen = turtle.getscreen()
gur = turtle.Turtle()
gur.speed(4)
for x in range(sides):
    gur.fd(length)
    angle = 360/sides
    gur.left(angle)
gur.penup()
gur.goto(-200,-200)
gur.pendown()
for x in range(sides):
    gur.circle(sides)
    gur.speed(sides)
    gur.fd(70)
    gur.right(200-length)
    gur.fd(100)
    
