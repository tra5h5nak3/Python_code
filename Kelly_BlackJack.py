import random
dealer_cards = []                   # Dealer's hand
player_cards = []                   # Player's hand
player_points = 0
dealer_points = 0
scoreboard =  ("Dealer Points: " , dealer_points , "Player Points: " , player_points )

def playerClean(player_cards):          # W3 Schools helped me with proper syntax on this function
    player_cards = []                   # These functions clears the hands of both player and dealer
    return player_cards
def dealerClean(dealer_cards):
    dealer_cards = []
    return dealer_cards

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,14))       # TechBytes io showed me this while command
while len(player_cards) != 2:                       # Both hands draw
    player_cards.append(random.randint(1,14))
    
if sum(player_cards) > 21:                          # Checks if player busted
    print("Dealer Points: " , dealer_points , "Player Points: " , player_points )
    print("Dealer has H and ", dealer_cards[1])
    print("You have ", player_cards)
    print("You Busted")
    dealer_points += 1
    player_cards = playerClean(player_cards)        # Starts a new round
    dealer_cards = dealerClean(dealer_cards)

if sum(dealer_cards) == 21:                         # Dealer wins instantly if they get 21 from draw
    print("Dealer Points: " , dealer_points , "Player Points: " , player_points )
    print("Dealer has H and ", dealer_cards[1])
    print("You have ", player_cards)
    print("The Dealer has 21 and wins! \n ")
    dealer_points += 1
    player_cards = playerClean(player_cards)        # Starts a new round
    dealer_cards = dealerClean(dealer_cards)
elif sum(dealer_cards) > 21:
    print("Dealer Points: " , dealer_points , "Player Points: " , player_points )
    print("Dealer has H and ", dealer_cards[1])
    print("You have ", player_cards)
    print("Dealer has busted \n ")
    player_points += 1
    player_cards = playerClean(player_cards)        # Starts a new round
    dealer_cards = dealerClean(dealer_cards)
    
while (player_points) < 10 and (dealer_points) < 10:    
    if len(player_cards) == 0:
        player_cards = []
        player_cards.append(random.randint(1,14))       # Gives player cards if hand empty
        player_cards.append(random.randint(1,14))       # Got this idea of card setup from Kevin Olson
    if len(dealer_cards) == 0:
        dealer_cards = []
        dealer_cards.append(random.randint(1,14))       # Gives dealer cards if hand empty
        dealer_cards.append(random.randint(1,14)) 
        
    print("Dealer Points:" , dealer_points , " Player Points:" , player_points ) # Shows player their cards before the question
    print("Dealer has H and ", dealer_cards[1])
    print("You have ", player_cards)
    action_taken = str(input("Do you want to stay or hit? "))       # Ask player if they want to hit
    if action_taken == "hit":
        player_cards.append(random.randint(1,14))                   # Draws card if they type "hit"
        print (" \n You have a total of " + str(sum(player_cards)) + " from these cards " ,player_cards)
        if sum(player_cards) > 21:
            print("You busted \n ")
            dealer_points += 1
            player_cards = playerClean(player_cards)        # Starts a new round
            dealer_cards = dealerClean(dealer_cards)
        if sum(dealer_cards) > 21:
            print("Dealer Points: " , dealer_points , "Player Points: " , player_points )
            print("Dealer has ", dealer_cards)
            print("You have ", player_cards)
            print("Dealer has busted \n ")
            player_points += 1
            player_cards = playerClean(player_cards)        # Starts a new round
            dealer_cards = dealerClean(dealer_cards)
    else:
        while sum(dealer_cards) < 16:                       # If dealer sum is less than 16 the dealer will hit
            dealer_cards.append(random.randint(1,14))
            print("Dealer Hits")
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with" , player_cards)
        if sum(dealer_cards) > 21:                                  # Checks to see if dealer busted
            print("Dealer Points: " , dealer_points , "Player Points: " , player_points )
            print("Dealer has ", dealer_cards)
            print("You have ", player_cards)
            print("Dealer has busted \n ")
            player_points += 1
            player_cards = playerClean(player_cards)    # Starts a new round
            dealer_cards = dealerClean(dealer_cards)
        elif sum(dealer_cards) >= sum(player_cards):           # Compares both sums and chooses winner
            print ("Dealer wins! \n ")
            dealer_points += 1
            player_cards = playerClean(player_cards)        # Starts a new round
            dealer_cards = dealerClean(dealer_cards)
        else:
            print("You win! \n ")
            player_points += 1
            player_cards = playerClean(player_cards)        # Starts a new round
            dealer_cards = dealerClean(dealer_cards)

if (player_points) == 10:                               # First point system to reach 10 points ends the program
    print("Dealer Points: " , dealer_points , "Player Points: " , player_points )
    print("You won the game")
if (dealer_points) == 10 :
    print("Dealer Points: " , dealer_points , "Player Points: " , player_points )
    print ("Dealer won the game")
