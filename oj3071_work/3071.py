"""This code will find how many numbers in a set can be divided by a number and get """
A = int(input())
B = int(input())
d = int(input())
r = int(input())
count = 0
for i in range(A,B+1):
    if i % d == r:
        count += 1
print(count)
