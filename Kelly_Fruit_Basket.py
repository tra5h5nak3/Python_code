"""  
Student Name: Bryce Kelly
Period: 6

Program purpose: Compute the cost os c fruit basket 

1. Significant constants
       cost the fruit (bannas, apples, oranges)
2. The inputs are
       user requests number of apples, oranges or bannas
       user name
       user ranking of the shopping experience
3. Computations:
       number or amount of fruit * cost of the item
       total cost = cost of bannas, apples, oranges
       cost per item = total cost / total items
        
4. The outputs are
       Print line showing the total cost
       Print line showing cost per item
       satisifaction rating:  A number between 1 and 10
       

Example output
    The total cost of John Smiths's basket is $3.73.   Note John Smith is the user name
    The cost per item is $0.73.

"""
# Initialize the constants
Bannas_cost = 0.24
Apple_cost = 1.19
Orange_cost = 0.95

Name = input("Enter username: ")
Apples  = float(input("Enter number of apples purchased"))
Bannas = float(input("Enter number of bannas purchased"))
Oranges = float(input("Enter number of oranges purchased"))

totalCost = ((Apple_cost * Apples) + (Bannas * Bannas_cost) + (Oranges * Oranges_cost))
costPerItem = (totalCost / (Apples + Bannas + Oranges))

print(f"The total cost of {Name}'s basket is ${totalCost}.")
print(f"The cost per item {round(costPerItem,2)}.")

Satisfaction = input("On a scale of 1-10, how would you rate your expirence here: ")
print(f"Your satisfaction level was: {Satisfaction}")

