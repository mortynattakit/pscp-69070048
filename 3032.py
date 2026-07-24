"""This code will find who gets the highest score in the class 
and how many people get the top score"""
people = int(input())
highest = 0
count = 1
for i in range(people):
    score = int(input())
    if score > highest:
        highest = score
        count = 1
        i += 0
    elif score == highest:
        count += 1
print(highest, count, sep="\n")
