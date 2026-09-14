"""this code check whether whose birthday is earlier"""
from datetime import date

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

diff = (date2 - date1).days

if abs(diff) <= 7:
    print(0)
elif diff > 0:
    print(1)
else:
    print(2)
