"""This code counts how many odd and even numbers 
from 3 numbers user input"""
even = 0
odd = 0
for _ in range(3):
    num = int(input())
    if not num % 2:
        even += 1
    else:
        odd += 1
print(even,odd,sep="\n")
