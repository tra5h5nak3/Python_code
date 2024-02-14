# Bryce Kelly
# COP 2500
# Final_Project
# Nov 16, 2022
import random

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }

board2 ={'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }

board_list = []
for item in board.keys():
    board_list.append(item)


def print_board(x):
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
    print("-----")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-----")
    print(board["7"]+"|"+board["8"]+"|"+board["9"])

    

print('''This is where each number correlates on the board
          1|2|3
          4|5|6
          7|8|9''')

intro = '''Welcome to fantasy tic tac toe football! You can choose one of seven
florida football college teams. Please select team from below.
1.) UCF Knights
2.) FAU Owls
3.) FIU Panthers
4.) FSU Seminoles
5.) USF Bulls
6.) UF  Gators
7.) UM  Hurricanes'''
print(intro)
team = input("")
if team == "1":
    team = "UCF Knights"
elif team == "2":
    team = "FAU Owls"
elif team == "3":
    team = "FIU Panthers"
elif team == "4":
    team = "FSU Seminoles"
elif team == "5":
    team = "USF Bulls"
elif team == "6":
    team = "UF Gators"
elif team == "7":
    team = "UM Hurricanes"
print("Your team is the " + team)
sym = input("What would you like your symbol to be?\n")
esym = input("What would you like the AI symbol to be?\n")
print ("Your symbol is "+ sym + "\nThe AI symbol is "+ esym)


def game():
    
    count = 0
    win = False
    winner = "Error"
    
    while win == False:
        if count >= 5:
            if board["1"] == board["2"] == board["3"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["1"] == board["2"] == board["3"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["4"] == board["5"] == board["6"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["4"] == board["5"] == board["6"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["7"] == board["8"] == board["9"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["7"] == board["8"] == board["9"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["1"] == board["4"] == board["7"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["1"] == board["4"] == board["7"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["2"] == board["5"] == board["8"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["2"] == board["5"] == board["8"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["3"] == board["6"] == board["9"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["3"] == board["6"] == board["9"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["1"] == board["5"] == board["9"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["1"] == board["5"] == board["9"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["3"] == board["5"] == board["7"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["3"] == board["5"] == board["7"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
        print_board(board)
        turn = input("Where would you like go?\n")
        if board[turn] == " ":
            board[turn] = sym
            count += 1
            x = str(turn)
            
            board_list.remove(x)
        else:
            print("Error, spot is unavalible.\nPick another")
            continue
        if count >= 5:
            if board["1"] == board["2"] == board["3"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["1"] == board["2"] == board["3"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["4"] == board["5"] == board["6"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["4"] == board["5"] == board["6"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["7"] == board["8"] == board["9"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["7"] == board["8"] == board["9"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["1"] == board["4"] == board["7"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["1"] == board["4"] == board["7"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["2"] == board["5"] == board["8"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["2"] == board["5"] == board["8"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["3"] == board["6"] == board["9"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["3"] == board["6"] == board["9"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["1"] == board["5"] == board["9"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["1"] == board["5"] == board["9"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
            elif board["3"] == board["5"] == board["7"] == sym:
                print("\nGame Over. \n")
                print(team +" Won\n")
                winner = team
                print_board(board)
                break
            elif board["3"] == board["5"] == board["7"] == esym:
                print("\nGame Over. \n")
                print(esym +" Won\n")
                winner = esym
                print_board(board)
                break
        if count == 9:
            print("\nGame Over. \n")
            print("Tie Game!\n")
            print_board(board)
    
        num = str(random.choice(board_list))
        
        if board[num] == " ":
            board[num] = esym
            count += 1
            x = str(num)
            board_list.remove(x)
        else:
            num = str(random.choice(board_list))
            board[num] = esym
            count += 1
            x = str(num)
            board_list.remove(x)
            continue
    return (winner)

print('''--------------------------------\n\nTOURNAMENT CHART 

UCF vs FAU ----- 

		 \ 

		   xxxxxxx  --------- 

		 /		     \ 

FIU vs FSU ------		       \ 

				         xxxxxxxxx 

USF vs UM -------		       / 

		  \		     / 

		   xxxxxxxx ---------

		  / 

  UF 	---------- \n\n--------------------------------''')


if team == "UCF Knights":
    print("Your first opponent is "+ "FAU Owls" )
    suc=game()
    
    if suc == "UCF Knights":
        print("Your team won!")
        ran = random.randint(1,2)
        if ran == 1:
            gat = "FIU Panthers"
        else:
            gat = "FSU Seminoles"
        print("Your next opponent is "+ gat )
        board_list = []
        for item in board.keys():
            board_list.append(item)
        board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                 '4': ' ' , '5': ' ' , '6': ' ' ,
                 '7': ' ' , '8': ' ' , '9': ' ' }
        
        suc = game()
        if suc == "UCF Knights":
            ran = random.randint(1,3)
            if ran == 1:
                gat = "USF Bulls"
            elif ran ==2:
                gat = "UM Hurricanes"
            else:
                gat = "UF Gators"
            print("Your next opponent is "+ gat )
            board_list = []
            for item in board.keys():
                board_list.append(item)
            board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                     '4': ' ' , '5': ' ' , '6': ' ' ,
                     '7': ' ' , '8': ' ' , '9': ' ' }
            
            suc = game()
            if suc == "UCF Knights":
                print(team+" WON THE CHAMPIONSHIP!")
            else:
                print("You lost the tournament!")
        else:
            print("You lost the tournament!")
    else:
        print("You lost the tournament!")
if team == "FAU Owls":
    print("Your first opponent is "+ "UCF Knights" )
    suc=game()
    if suc == "FAU Owls":
        print("Your team won!")
        ran = random.randint(1,2)
        if ran == 1:
            gat = "FIU Panthers"
        else:
            gat = "FSU Seminoles"
        print("Your next opponent is "+ gat )
        board_list = []
        for item in board.keys():
            board_list.append(item)
        board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                  '4': ' ' , '5': ' ' , '6': ' ' ,
                  '7': ' ' , '8': ' ' , '9': ' ' }
        suc = game()
        if suc == "FAU Owls":
            ran = random.randint(1,3)
            if ran == 1:
                gat = "USF Bulls"
            elif ran ==2:
                gat = "UM Hurricanes"
            else:
                gat = "UF Gators"
            print("Your next opponent is "+ gat )
            board_list = []
            for item in board.keys():
                board_list.append(item)
            board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                     '4': ' ' , '5': ' ' , '6': ' ' ,
                     '7': ' ' , '8': ' ' , '9': ' ' }
            suc = game()
            if suc == "FAU Owls":
                print(team+" WON THE CHAMPIONSHIP!")
            else:
                print("You lost the tournament!")
        else:
            print("You lost the tournament!")
    else:
        print("You lost the tournament!")
if team == "FIU Panthers":
    print("Your first opponent is "+ "FSU Seminoles")
    suc=game()
    if suc == "FIU Panthers":
        print("Your team won!")
        ran = random.randint(1,2)
        if ran == 1:
            gat = "UCF Knights"
        else:
            gat = "FAU Owls"
        print("Your next opponent is "+ gat )
        board_list = []
        for item in board.keys():
            board_list.append(item)
        board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                  '4': ' ' , '5': ' ' , '6': ' ' ,
                  '7': ' ' , '8': ' ' , '9': ' ' }
        
        suc = game()
        if suc == "FIU Panthers":
            ran = random.randint(1,3)
            if ran == 1:
                gat = "USF Bulls"
            elif ran ==2:
                gat = "UM Hurricanes"
            else:
                gat = "UF Gators"
            print("Your next opponent is "+ gat )
            board_list = []
            for item in board.keys():
                board_list.append(item)
            board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                     '4': ' ' , '5': ' ' , '6': ' ' ,
                     '7': ' ' , '8': ' ' , '9': ' ' }
            suc = game()
            if suc == "FIU Panthers":
                print(team+" WON THE CHAMPIONSHIP!")
            else:
                print("You lost the tournament!")
        else:
            print("You lost the tournament!")
    else:
        print("You lost the tournament!")
if team == "FSU Seminoles":
    print("Your first opponent is "+ "FIU Panthers" )
    suc=game()
    if suc == "FSU Seminoles":
        print("Your team won!")
        ran = random.randint(1,2)
        if ran == 1:
            gat = "UCF Knights"
        else:
            gat = "FAU Owls"
        print("Your next opponent is "+ gat )
        board_list = []
        for item in board.keys():
            board_list.append(item)
        board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                 '4': ' ' , '5': ' ' , '6': ' ' ,
                 '7': ' ' , '8': ' ' , '9': ' ' }
        suc = game()
        if suc == "FSU Seminoles":
            ran = random.randint(1,3)
            if ran == 1:
                gat = "USF Bulls"
            elif ran ==2:
                gat = "UM Hurricanes"
            else:
                gat = "UF Gators"
            print("Your next opponent is "+ gat )
            board_list = []
            for item in board.keys():
                board_list.append(item)
            board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                     '4': ' ' , '5': ' ' , '6': ' ' ,
                     '7': ' ' , '8': ' ' , '9': ' ' }
            suc = game()
            if suc == "FSU Seminoles":
                print(team+" WON THE CHAMPIONSHIP!")
            else:
                print("You lost the tournament!")
        else:
            print("You lost the tournament!")
    else:
        print("You lost the tournament!")
if team == "USF Bulls":
    print("Your first opponent is "+ "UM Hurricanes")
    suc=game()
    if suc == "USF Bulls":
        print("Your team won!")
        print("Your next opponent is "+ "UF Gators" )
        board_list = []
        for item in board.keys():
            board_list.append(item) 
        board= {'1': ' ' , '2': ' ' , '3': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '7': ' ' , '8': ' ' , '9': ' ' }
        suc = game()
        if suc == "USF Bulls":
            print("Your team won!")
            ran = random.randint(1,4)
            if ran == 1:
                gat = "UCF Knights"
            elif ran == 2:
                gat = "FAU Owls"
            elif ran == 3:
                gat = "FIU Panthers"
            else:
                gat = "FSU Seminoles"
            print("Your next opponent is " + gat )
            board_list = []
            for item in board.keys():
                board_list.append(item)
                
            board= {'1': ' ' , '2': ' ' , '3': ' ' ,
                    '4': ' ' , '5': ' ' , '6': ' ' ,
                    '7': ' ' , '8': ' ' , '9': ' ' }
            suc = game()
            if suc == "USF Bulls":
                print(team+" WON THE CHAMPIONSHIP!")
            else:
                print("You lost the tournament!")
        else:
            print("You lost the tournament!")
        
    else:
        print("You lost the tournament!")
if team == "UM Hurricanes":
    print("Your first opponent is "+ "USF Bulls" )
    board_list = []
    for item in board.keys():
        board_list.append(item)
    board = {'1': ' ' , '2': ' ' , '3': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '7': ' ' , '8': ' ' , '9': ' ' }
    board = board2
    suc=game()
    if suc == "UM Hurricanes":
        print("Your team won!")
        print("Your next opponent is "+ "UF Gators" )
        board_list = []
        for item in board.keys():
            board_list.append(item)
        board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                 '4': ' ' , '5': ' ' , '6': ' ' ,
                 '7': ' ' , '8': ' ' , '9': ' ' }
        suc = game()
        if suc == "UM Hurricanes":
            print("Your team won!")
            ran = random.randint(1,4)
            if ran == 1:
                gat = "UCF Knights"
            elif ran == 2:
                gat = "FAU Owls"
            elif ran == 3:
                gat = "FIU Panthers"
            else:
                gat = "FSU Seminoles"
            print("Your next opponent is " + gat )
            board_list = []
            for item in board.keys():
                board_list.append(item)
            board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                     '4': ' ' , '5': ' ' , '6': ' ' ,
                     '7': ' ' , '8': ' ' , '9': ' ' }
            suc = game()
            if suc == "UM Hurricanes":
                print(team+" WON THE CHAMPIONSHIP!")
            else:
                print("You lost the tournament!")
        else:
            print("You lost the tournament!")
    else:
        print("You lost the tournament!")


if team == "UF Gators":
    ran = random.randint(1,2)
    if ran == 1:
        gat = "USF Bulls"
    else:
        gat = "UM Hurricanes"
    print("Your first opponent is "+ gat)
    board_list = []
    for item in board.keys():
        board_list.append(item)
    board = {'1': ' ' , '2': ' ' , '3': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '7': ' ' , '8': ' ' , '9': ' ' }
    suc = game()
    if suc == "UF Gators":
        print("Your team won!")
        board_list = []
        for item in board.keys():
            board_list.append(item)
        board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                 '4': ' ' , '5': ' ' , '6': ' ' ,
                 '7': ' ' , '8': ' ' , '9': ' ' }
        suc = game()
        if suc == "UF Gators":
            print("Your team won!")
            ran = random.randint(1,4)
            if ran == 1:
                gat = "UCF Knights"
            elif ran == 2:
                gat = "FAU Owls"
            elif ran == 3:
                gat = "FIU Panthers"
            else:
                gat = "FSU Seminoles"
            print("Your next opponent is " + gat )
            board_list = []
            for item in board.keys():
                board_list.append(item)
            board = {'1': ' ' , '2': ' ' , '3': ' ' ,
                     '4': ' ' , '5': ' ' , '6': ' ' ,
                     '7': ' ' , '8': ' ' , '9': ' ' }
            suc = game()
            if suc == "UF Gators":
                print(team+" WON THE CHAMPIONSHIP!")
            else:
                print("You lost the tournament!")
        else:
            print("You lost the tournament!") 
    else:
        print("You lost the tournament!")
        

    








        



















