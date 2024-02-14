# Bryce Kelly
# COP 2500 0v64
# BeachThemepark.py
# Sept 9, 2022

choice= (str(input("Where do you want to go?\n")))

if choice == "beach" or choice == "Beach":
    bb= int(input("How many beach balls are you bringing?\n"))
    if bb >= 5:
        print("You are well prepared")
    else:
        print("Are you sure you have enough?")
elif choice == "Themepark" or "themepark" or "Theme park" or "theme park":
    people = int(input("How many people are going to be at the park\n"))
    if people >= 1000:
        print("This is too crowded")
    elif people >= 500:
        print("It's going to be busy")
    elif people >= 100:
        print("It's a light day")
    elif people >= 0:
        print("Nobody is here")
    else:
        print("Nobody is here")
