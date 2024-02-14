# Kyle Dencker
# COP 2500C
# Left Right Game
# Sep 14, 2022

import random

board = []
sets = 4
for num in range(sets):
    board.append(random.randint(1, 9))
    board.append(random.randint(1, 9))

turn = 0
kyle = 0
cop2500 = 0

while (len(board) != 0):
    print()
    print("Player", turn%2+1, "turn")
    for index in range(len(board)):
        print(board[index], end=" ")
    print()
    print("Kyle:", kyle)
    print("Class:", cop2500)
    choice = input("Left or Right?")

    if (choice == "Left"):
        if (turn%2 == 0):
            kyle+=board[0]
            board.pop(0)
            turn+=1
        else:
            cop2500 += board[0]
            board.pop(0)
            turn+=1
    elif(choice == "Right"):
        if (turn%2 == 0):
            kyle+=board[-1]
            board.pop(-1)
            turn+=1
        else:
            cop2500 += board[-1]
            board.pop(-1)
            turn+=1
    
print("Game over")
if (kyle > cop2500):
    print("Told you Kyle wins all the time")
    print("Kyle beat you by", kyle-cop2500)
elif(kyle==cop2500):
    print("We tied... Ok")
else:
    print("Will never happen.")
