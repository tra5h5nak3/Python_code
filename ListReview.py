# Kyle Dencker
# COP 2500C
# Oct 26, 2022
# Loop/List Review

item_list = ['apples', 'bananas', 'orange']

# Ban oranges. :)

for i in range(len(item_list)):
    if (item_list[i] == 'orange'):
        item_list[i] = "Banned"

print(item_list)

test_questions = [3, 5, 7, 9, 11]
for i in range(len(test_questions)):
    test_questions[i] += 1

print(test_questions)

numbers = [4, 2, 7, 9, 9, 7, 3, 6, 8, 11]
newer_list = []
# 15, 10, 13, 12, 16

for i in range(len(numbers)//2):
    new_value = numbers[i] + numbers[-1-i]
    newer_list.append(new_value)
print(newer_list)

# This thought process must be done in C. 
for i in range(len(numbers)//2):
    list_length = len(numbers)
    new_value = numbers[i] + numbers[list_length-1-i]
    newer_list.append(new_value)
print(newer_list)
