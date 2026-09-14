"""THis code will help calculate discount for members and when """
import math

yesno = input()
goods = int(input())
price = 0
for _ in range(goods):
    price += float(input())

if yesno == "Y":
    price *= 0.95
elif yesno == "N" and price >= 500:
    price *= 0.97

print(f"{(math.ceil(price * 100) / 100):.2f}")
