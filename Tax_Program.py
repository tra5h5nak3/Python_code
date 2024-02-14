"""  (This is another way to do comments)
Program purpose: Compute a person's income tax.

1. Significant constants
       tax rate
       standard deduction
       deduction per dependent
2. The inputs are
       gross income 
       number of dependents 
3. Computations:
       taxable income = gross income - the standard deduction - 
                        a deduction for each dependent 
       income tax = is a fixed percentage of the taxable income 
4. The outputs are
       Print line showing the income tax

For testing use the following
    grossIncome = 45520.36
    numDependents = 2

"""

# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 3000.00
               
# Request the inputs
grossIncome = float(input("Enter the gross income: "))  #This is example of how to get user input
numDependents = int(input("Enter the number of dependents: "))   

# Compute the income tax
taxableIncome = (grossIncome - STANDARD_DEDUCTION)-(DEPENDENT_DEDUCTION * numDependents)
incomeTax = taxableIncome * TAX_RATE
         
# Display the income tax
print(f"The income tax is ${incomeTax}") # this is new in Python3.7 called fprint allows you to include variables in a print statement 


      