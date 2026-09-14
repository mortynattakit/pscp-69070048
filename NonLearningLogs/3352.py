"""THis code get list of nums and have to print the last num of each"""
nums = input().strip("[]").split(",")
for i in nums:
    print(i[-1] if len(i) > 0 else i[0])
