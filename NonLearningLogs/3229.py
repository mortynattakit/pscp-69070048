"""This code will calculate points"""
base = int(input())
bonus = int(input())
day = int(input())

if day > 3:
    MULT = 1.5
else:
    MULT = 1

total = (base + bonus) * MULT

if total >= 1500:
    RANK = 5
elif total >= 1000:
    RANK = 4
elif total >= 500:
    RANK = 3
elif total >= 200:
    RANK = 2
else:
    RANK = 1

if RANK == 5 and day >= 7:
    STATUS = 99
elif RANK == 4 and bonus > 300:
    STATUS = 88
else:
    STATUS = 0

print(int(total))
print(RANK)
print(STATUS)
