"""THis code will find the price after discount"""
priceperbottle = int(input())
bottlesfordiscount = int(input())
discountprice = int(input())
bottlesbought = int(input())

price = bottlesbought * priceperbottle

if bottlesfordiscount == 0:
    print(price)
else:
    