"""THis code will find the price after discount"""
priceperbottle = int(input())
bottlesfordiscount = int(input())
discountprice = int(input())
bottlesbought = int(input())

price = 0
caps = 0
bottles = 0

while bottles < bottlesbought:
    if 0 < bottlesfordiscount <= caps:
        price += discountprice
        caps -= bottlesfordiscount
    else:
        price += priceperbottle
    bottles += 1
    caps += 1
print(price)
