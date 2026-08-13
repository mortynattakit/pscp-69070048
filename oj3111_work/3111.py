"""THis code will help calculate discount for members and when """
import math
yesno = input()
goods = int(input())
price = 0
for _ in range(goods):
    _ += 0
    price += float(input())
if yesno == "Y":
    print(f"{((math.ceil((95/100) * price) * 100) / 100):.2f}")
elif yesno == "N" and price >= 500:
    print(f"{((math.ceil((97/100) * price) * 100) / 100):.2f}")
else:
    print(f"{(math.ceil(price) * 100) / 100}")
