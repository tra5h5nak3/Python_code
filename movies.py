# Bryce Kelly
# COP 2500 0v64
# movies.py
# Sept 13, 2022

#smc = str(input("Are you a Small Monster Collector\n"))

people = int(input("How many moviegoers?\n"))


if people > 25:
    total = people * 7.25
    print("The total ticket price is $"+"%.2f"%(total))
else:
    people -= 1
    total = people * 12.00
    total += 9.50
    print("The total ticket price is $"+"%.2f"%(total))
