"""This code will print triangle out which the margin will be 0 and inside is 1"""
num = int(input())
for i in range(num):
    for j in range(i + 1):
        if not j or j == i or i == num-1:
            print(0, end="")
        else:
            print(1, end="")
    print()
