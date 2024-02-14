# for testing codes
""""
Program Description: Using the supplied list of grades gradeList
Calculate the nubmber of A's, B's, C', D's and F's 

A is 90 or above
B is 80 to 89
C is 70 to 79
D is 60 to 69
F all other

Inputs:
gradeList

Outputs:
Overal mean, mode and total number of scores
# of A, B, C, D, and F's and the average score for each


"""
import statistics

# sample data
gradeList = [65, 85, 55, 57, 68, 75, 90, 90, 63, 66, 77, 77, 61, 76, 80, 69, 55, 66, 
99, 60, 82, 96, 98, 67, 57, 67, 97, 88, 68, 90, 89, 57, 65, 69, 98, 61, 73, 91, 89, 
61, 96, 77, 58, 83, 90, 67, 90, 60, 78, 92]

#starter code to work with it is not complete and has missing
# elements that need to be added

Acount = 0
Bcount = 0
Ccount = 0
Dcount = 0
Fcount = 0


Alist=[]
Blist=[]
Clist=[]
Dlist=[]
Flist=[]


for grade in gradeList:
    if grade >= 90:
        Acount+=1
        Alist.append(grade)
    elif grade>=80 and grade==89:
        Bcount+=1
        Blist.append(grade)
    elif grade>=70 and grade<79:
        Ccount+=1
        Clist.append(grade)
    elif grade>=60 and grade<69:
        Dcount+=1
        Dlist.append(grade)
    elif grade<60:
        Fcount+1
        Flist.append(grade)



# Outputs
print(f"The mean score was {statistics.mean(gradeList)}.")
print(f"The mode score was {statistics.mode(gradeList)}.")
print(f"The total number of socres is {len(gradeList)}")

# total number of A's and the average A score
print(f"Total number of A's was {Acount} and the average was {statistics.mean(Alist)}%")
# total number of B's and the average B score
print(f"Total number of B's was {Bcount} and the average was {statistics.mean(Blist)}%")
# total number of C's and the average C score
print(f"Total number of C's was {Ccount} and the average was {statistics.mean(Clist)}%")
# total number of D's and the average D score
print(f"Total number of D's was {Dcount} and the average was {statistics.mean(Dlist)}%")
# total number of F's and the average F score
print(f"Total number of F's was {Fcount} and the average was {statistics.mean(Flist)}%")

