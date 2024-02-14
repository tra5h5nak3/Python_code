# Bryce Kelly
# COP 2500
# 5.1 Functions
# Nov 11, 2022

import math

import turtle

import random
def distance(x, y):
    b = x * x
    c = y * y
    d = math.sqrt(b+c)
    return d
    

# Starter Code

def randomTurtle():

    for count in range(10):

        choice = random.randint(1,2)

    if (choice==1):

        turtle.forward(random.randint(5, 50))

    elif(choice==2):

        turtle.right(random.randint(1,359))
    x2= turtle.xcor()
    y2=turtle.ycor()
    print (distance(x2, y2))


def testTurtle():
    

    turtle.forward(100)

    turtle.left(90)

    turtle.forward(100)
   
# Call this when turning it in

randomTurtle()

# Call this when testing to make sure you have the correct answer
















