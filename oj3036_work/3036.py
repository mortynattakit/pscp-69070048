"""This code will calculate whats the minimum steps to walk from the selected number to 1"""
import math
selectednum = int(input())
floor = math.ceil(math.sqrt(selectednum))

if (not floor % 2 and not selectednum % 2) or (floor % 2 and selectednum % 2):
    print((floor - 1) * 2)
else:
    print(((floor - 2) * 2) + 1)
