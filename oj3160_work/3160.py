"""This code let user input start and end num and output all prime and how many prime are there"""
def prime(n):
    """this subroutine is used for checking whether the number is prime or not"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if not n % 2 or not n % 3:
        return False
    num = 5
    while num * num <= n:
        if not n % num or not n % (num+2):
            return False
        num += 6
    return True

start,end = map(int, input().split())

primes = []
for i in range(start, end+1):
    if prime(i):
        primes.append(i)
if primes:
    print(*primes)
print(f"Total primes: {len(primes)}")
