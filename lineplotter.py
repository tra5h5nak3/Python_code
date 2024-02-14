# Bryce Kelly
# COP 2500 0v64
# lineplotter.py
# Oct 4, 2022

slope = float(input("Whats the slope?\n"))
cept = float(input("Whats the intercept\n"))
x = 0
ten = 10
def plot(a,b):
    y = (a * x) + b
    return y
for num in range(0,10,1):
    sentence = "At x = {}, y = {}"
    print(sentence.format(num,plot(slope,cept)))
    x += 1
x = 10
for num in range(5):
    sentence = "At x = {}, y = {}"
    print(sentence.format(ten,plot(slope,cept)))
    x = x * 10
    ten = ten * 10
