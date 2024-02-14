# Bryce Kelly
# COP 2500C
# assignment 4.1
# Nov 4, 2022

def clean(x):
    cl = []
    for i in x:
        y = i.lower()
        y = y.strip()
        y = y.capitalize()
        cl.append(y)
    return (cl)

classes =[]
while len(classes) != 5:
    count = 0
    classes = clean(classes)
    if len(classes) != 0:
        print("you are currently taking these courses")
        for item in classes:
            count +=1
            print (count, ".", item)
        count = 0



    
    if len(classes) == 0:
        print("You are currently not enrolled in any courses")
    if len(classes) > 5:

        ans= input("What courses would you like to drop?\n")
        ans = list(ans.split(","))
        for i in ans:
            y = i.lower()
            y = y.strip()
            y = y.capitalize()
            
            if y in classes:
                classes.remove(y)
            else:
                continue
        
    else:
        #
        choice = input("What courses would you like to take?\n")
        choice = list(choice.split(","))
        for i in choice:
            classes.append(i)
classes = clean(classes)

print("you are currently taking these courses")
count = 0
for item in classes:
    count +=1
    print (count, ".", item)
print("Done!")
        

        

    



