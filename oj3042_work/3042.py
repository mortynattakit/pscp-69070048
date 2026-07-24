"""This code will divide the input to make it divisible by 10 and then minus it by 10 till 0"""
n = int(input())
n //= 10
n *= 10

while n > 0:
    print(n, end=" ")
    n -= 10
print("0")
