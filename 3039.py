"""this code will find which number is the lowest based on the numbers the user inputs"""
nums = int(input())
for i in range(nums):
    a = int(input())
    if not i:
        lowest = a
    else:
        if a < lowest:
            lowest = a
print(lowest)
