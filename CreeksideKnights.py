RunTime = float(input("How many times do you want this to run?"))
ck = "CREEKSIDE"
Kn = "KNIGHTS"

list = []
while RunTime > 0:
    numInpt = int(input("Enter Number"))
    numInptOrin = numInpt
    numInpt %= 3
    if numInpt == 0:
        list.append("CREEKSIDE")
    numInpt = numInptOrin
    numInpt %= 7
    if numInpt == 0:
        list.append("KINGHTS")
    numInpt = numInptOrin
    numInpt %= 3
    numInpt %= 7
    if numInpt != 0:
        list.append(numInptOrin)
    RunTime -= 1
for number in list:
    print(number)