"""This code will calculate the inflation"""
from decimal import Decimal, ROUND_DOWN, getcontext

getcontext().prec = 9999

n = Decimal(input())
k = int(input())

for _ in range(k):
    n += n * Decimal('0.0381')
    n = n.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
print(f"{n:.2f}")
