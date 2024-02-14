# Bryce Kelly
# COP 2500 0v64
# pizzacalc.py
# Sept 9, 2022

pizza  = int(input("How many pizzas do you want to order?\n"))
people = int(input("How many people are with you?\n"))


slices= pizza * 8
x= slices%people


if x == 0:
    spp= slices/people
    spp= int(spp)
    print("everyone gets",spp,"Slice!")
else:
    print("No pizza for anyone! Since you don't wanna be fair!")

            
