# Bryce Kelly
# COP 2500 0v64
# ScienceCenter.py
# Sept 21, 2022


choice = input("Go to Theme Park or Science Center?\n")
choice = choice.lower().strip()


if choice == "theme park":
    parks = int(input("How many parks are you going to?\n"))
    for num in range(1,parks +1,1):
        print("Day", num,",", "Park", num)
elif choice == "science center":
    x = False
    while x == False:
        z = input("Are you ready to leave?\n")
        z = z.lower().strip()
        if z == "ready":
            x = True

else:
    print("Type a real response!")

































