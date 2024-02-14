# Bryce Kelly
# COP 2500
# mastalist.py
# Oct 11, 2022

board = ["Rowing Event", "Halloween Dressup", "Food contest", "Donate Center", "Knightro Boxing"]
postings=["fitness bootcamp","food expeditor position","German language tutor","UCF scavenger hunt","roommate wanted","5k charity run"]
UCFlist=["Calculus Tutoring","Career Fair","Join the Soccer Team","Clothing Drive","Academic Schedule"]

xyz = board.copy()
abc = postings.copy()
lma = UCFlist.copy()

master_list_1 = []
master_list_2 = []
master_list_3 = []

# MASTER LIST ONE
master_list_1.extend(xyz+abc+lma)
print("MASTER LIST ONE")
print (master_list_1)
print("\n\n\n")


# MASTER LIST TWO
master_list_1.append("last")
for x in range(0,master_list_1.index("last")):
    if x >= len(xyz):
        pass
    else:
        master_list_2.append(xyz[x])
    if x >= len(abc):
        pass
    else:
        master_list_2.append(abc[x])
    if x >= len(lma):
        pass
    else:
        master_list_2.append(lma[x])
    if len(master_list_2) == master_list_1.index("last"):
        break
print("MASTER LIST TWO")
print(master_list_2)
print("\n\n\n")

# MASTER LIST THREE
master_list_3 = master_list_1.copy()
master_list_3.sort()
print("MASTER LIST THREE")
print(master_list_3)




