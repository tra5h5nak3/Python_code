# Bryce Kelly
# COP 2500
# lab_9.3
# Nov 6, 2022

def grade_up(grade_list):
    count = 0
    for i in range(len(grade_list)-1):   
        if grade_list[i] < grade_list[i+1]:
            count += 1            
    return count
newlist = []
semester = [[95, 92, 93, 96, 92],

            [100, 100],

            [70, 80, 90],

            [95, 85, 75, 70]]
for i in range(len(semester)):
    x = grade_up(semester[i])
    newlist.append(x)
print(newlist)
















