'''
Bryce Kelly
Period 6

'''
# Cost * Amount 
BananasAmtCst = 0
CucumbersAmtCst = 0
PeppersAmtCst = 0
ZucchiniAmtCst = 0
SweetOnionsAmtCst = 0
ChickenAmtCst = 0
GroundBeefAmtCst = 0
BreadAmtCst = 0
# Food  Cost Values
BananasCst = 0.24
CucumbersCst = 0.58
PeppersCst = 0.50
ZucchiniCst = 0.76
SweetOnionsCst = 1.10
ChickenCst = 2.78
GroundBeefCst = 2.25
BreadCst = 2.88
#Food Amounts
BananasAmt = 0
CucumbersAmt = 0
PeppersAmt = 0
ZucchiniAmt = 0
SweetonionAmt = 0
ChickenAmt = 0
GroundbeefAmt = 0
BreadAmt = 0
# This helps me do less typing
notEnough = "You dont have enough money."

reciept=[]

UserMon = float(input("How much money do you have? "))

while UserMon >= 0 :
    print("1. Buy Banana: 0.24")
    print("2. Buy Cucumber: 0.58 ")
    print("3. Buy Pepper: 0.50")
    print("4. Buy Zucchin: 0.76")
    print("5. Buy Sweet Onion: 1.10")
    print("6. Buy Chicken: 2.78")
    print("7. Buy Ground Beef: 2.25")
    print("8. Buy Bread: 2.88")
    print("9. Done shopping")

    choice = int(input("Enter Number"))

    if choice == 1:
        BananasAmt = float(input("How many bananas do you want?"))   #Changes the food amount to desired amount
        if UserMon < BananasCst * BananasAmt:
            print(notEnough) 
        else:
            BananasAmtCst = BananasAmt * BananasCst
            UserMon  = round(UserMon - BananasAmtCst,2)
            reciept.append(f"Bananas {round(BananasCst * BananasAmt,2)}")
        continue
    if choice == 2:
        CucumbersAmt = float(input("How many Cucumbers do you want?"))
        if UserMon < CucumbersCst * CucumbersAmt:
             print(notEnough)
        else:
            CucumbersAmtCst = CucumbersCst * CucumbersAmt
            UserMon = round(UserMon - CucumbersAmt * CucumbersCst,2)
            reciept.append(f"Cucumbers {round(CucumbersCst * CucumbersCst,2)}")
        continue
    if choice == 3:
        PeppersAmt = float(input("How many peppers do you want?"))
        if UserMon < PeppersAmt * PeppersCst:                                  # Makes sure user has enough money
             print(notEnough)
        else:
            PeppersAmtCst = PeppersAmt * PeppersCst
            UserMon = round(UserMon - PeppersAmt * PeppersCst,2)
            reciept.append(f"Peppers {round(PeppersCst * PeppersAmt,2)}")
        continue
    if choice == 4:
        ZucchiniAmt = float(input("How many Zucchini do you want?"))
        if UserMon < ZucchiniCst * ZucchiniAmt:
             print(notEnough)
        else:
            ZucchiniAmtCst = ZucchiniAmt * ZucchiniCst
            UserMon = round(UserMon - ZucchiniAmt * ZucchiniCst,2)
            reciept.append(f"Zucchini {round(ZucchiniCst * ZucchiniAmt,2)}")
        continue
    if choice == 5:
        SweetonionAmt = float(input("How many Sweet Onion do you want?"))
        if UserMon < SweetOnionsCst * SweetonionAmt:
             print(notEnough)
        else:
            SweetOnionsAmtCst = SweetOnionsCst * SweetonionAmt
            UserMon = round(UserMon - SweetonionAmt * SweetOnionsCst,2)
            reciept.append(f"Sweet Onions {round(SweetOnionsCst * SweetonionAmt,2)}")      # Adds item to the list called "Reciept"
        continue
    if choice == 6:
        ChickenAmt = float(input("How many Chickens do you want?"))
        if UserMon < ChickenCst * ChickenAmt:
             print(notEnough)
        else:
            ChickenAmtCst =  ChickenCst * ChickenAmt
            UserMon = round(UserMon - ChickenAmt * ChickenCst,2)
            reciept.append(f"Chickens {round(ChickenCst * ChickenAmt,2)}")
        continue
    if choice == 7:
        GroundbeefAmt = float(input("How many Ground Beef do you want?"))
        if UserMon < GroundBeefCst * GroundbeefAmt:
             print(notEnough)
        else:
            GroundBeefAmtCst = GroundBeefCst * GroundbeefAmt
            UserMon = round(UserMon - GroundbeefAmt * GroundBeefCst,2)
            reciept.append(f"Ground Beef {round(GroundBeefCst * GroundbeefAmt,2)}")
        continue
    if choice == 8:
        BreadAmt = float(input("How many Bread do you want?"))
        if UserMon < BreadCst * BreadAmt:
             print(notEnough)
        else:
            BreadAmtCst = BreadAmt * BreadCst
            UserMon = round(UserMon - BreadAmt * BreadCst,2)
            reciept.append(f"Bread {round(BreadCst * BreadAmt,2)}")
        continue
    if choice == 9:
        break 

print("-------------------------")
for item in reciept:
    print(item)
print("-------------------------")
print(f"Total due {round(BreadAmtCst + BananasAmtCst + CucumbersAmtCst + PeppersAmtCst + ZucchiniAmtCst + SweetOnionsAmtCst + ChickenAmtCst + GroundBeefAmtCst,2 )}")
print(f"Change Due {round(UserMon,2)}")
print("THANK YOU FOR SHOPPING")
print("-------------------------")









