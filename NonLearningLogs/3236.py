"""This code will input the amount of number and the 
digit of students' id and then check whether each digits add up to 9"""
num = int(input())
id1 = input()
id2 = input()

count = 0
for i in range(num):
    if int(id1[i]) + int(id2[i]) != 9:
        count += 1
print("YES" if not count else f"NO {count}")
