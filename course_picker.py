# Bryce Kelly
# COP 2500C
# assignment 3.1
# Oct 28, 2022

classes = []

print("Welcome to class registration!")
ans = input("Enter a course code:\n")
classes.append(ans)


while ans != "EXIT":
    count = 0
    
    print("You have registered in the following courses:\n")
    for item in classes:
        count +=1
        print (count, ".", item)

    if len(classes) >= 6:
        print("You have registered for too many courses. Pick one to delete")
        choice= int(input("Enter a number between 1 and 6\n"))
        if choice >= 7 or choice == 0:
            continue
        classes.pop(choice-1)
        
    else:
        pass
    ans = input("Enter a course code:\n")
    classes.append(ans)
print("Goodbye")           































