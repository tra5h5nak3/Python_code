





header = "Month    Starting Balance   Intrest Paid    Principle Paid   Payment   Ending Balance  Total Intrest"
PurchasePrice = float(input("What is the purchase price?"))
APR = float(input("What is the APR?"))
MonthlyPayment = float(input("What is monthly payment?"))
DownPayment = float(input("What is the down payment?"))
MonthlyIntRate = (APR/100)/12
Balance = PurchasePrice - DownPayment
# remaining = Balance -(MonthlyPayment-MonthlyIntRate)
# MonthlyInt = Balance * MonthlyIntRate
month = 0
totalInt = 0



print(header)

while Balance >= MonthlyPayment:
    month += 1
    if Balance < MonthlyIntRate:
        MonthlyInt = 0
        MonthlyPayment = Balance
    MonthlyInt = Balance * MonthlyIntRate
    PrinciplePaid = MonthlyPayment - MonthlyInt
    remaining = Balance - PrinciplePaid
    totalInt += MonthlyInt

    
    print("%2d  %19.2f  %12.2f  %12.2f  %16.2f  %12.2f %12.2f"%(month,Balance,MonthlyInt,PrinciplePaid,MonthlyPayment,remaining,totalInt))
    Balance =  remaining
month += 1
MonthlyInt = 0
MonthlyPayment = Balance
MonthlyInt = Balance * MonthlyIntRate
PrinciplePaid = MonthlyPayment - MonthlyInt
remaining = Balance - PrinciplePaid
totalInt += MonthlyInt

    
print("%2d  %19.2f  %12.2f  %12.2f  %16.2f  %12.2f %12.2f"%(month,Balance,MonthlyInt,PrinciplePaid,MonthlyPayment,remaining,totalInt))
Balance =  remaining





print(f"The total amount pf money paid is {round((PurchasePrice + totalInt),2)}.")
print(f"It took {month//12} years and {month%12} months")


