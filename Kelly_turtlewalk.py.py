import turtle

start=turtle.Turtle()  # creates turtle object for the starting point
start.shape('square')
start.color('green')
start.write('    Start')
stop1=turtle.Turtle()  # creates turtle object for the spot 1 point
stop1.shape('square')
stop1.color('blue')
stop1.penup()
stop1.setposition(125,100)
stop1.write('    Stop 1')
stop2=turtle.Turtle()  # creates turtle object for the spot 2 point
stop2.up()
stop2.shape('square')
stop2.color('purple')
stop2.setposition(175,-100)
stop2.write('    Stop 2')
end=turtle.Turtle()  # creates turtle object for the end point
end.up()
end.shape('triangle')
end.color('red')
end.setposition(-125,0)
end.write('   End')
# Do not change any of the above code

# Assignment: Create a turtle that goes to Stop1 then Stop 2 then to End BUT ONLY MAKES RIGHT HAND TURNS.  Make sure it leaves a trail.
# At End have it print out "Hello World"
# Name your file Lastname_turtleWalk.py
# 
# Put Your Name here  'Bryce Kelly
# Put your class period here  ' Period 6'

#Start your code here
Ark= turtle.Turtle()

Ark.color("Blue")  #sets color to blue

Ark.setheading(90)
Ark.forward(100)
Ark.right(90)
Ark.forward(175)
Ark.right(90)
Ark.forward(200)
Ark.right(90)
Ark.forward(300)
Ark.right(90)    #turns tutle right by 90
Ark.forward(100)

Ark.write("Hello World")



turtle.done() # make sure this is the last line in the code

