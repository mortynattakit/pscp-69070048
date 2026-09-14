"""THis code will calculate stat of coffee shop"""
import math
times = int(input())
sale = []
for _ in range(times):
    sale.append(int(input()))
print(sum(sale))
print(max(sale))
print(min(sale))
print(f"{(math.ceil(sum(sale)/len(sale)*10)/10):.1f}")
