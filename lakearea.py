# Bryce Kelly
# COP 2500 0v64
# lakearea.py
# Sept 8, 2022

# This program takes an user input called "radius" and finds the area
# of a half circle.

radius = int(input("What is the radius of the lake?\n"))

# Math for finding area of half circle
x = radius * radius
y = x * 3.1416
z = y/2

# rounding area so it can match example "127.2348"
z = round(z,4)

print("The area of the lake is", z)

