""""""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b == 0:
    print(d * a)
else:
    if not d % b:
        discountbottle = d // b - 1
        normalbottle = d - discountbottle
        price = (normalbottle * a) + (discountbottle * c)
        print(price)
    else:
        discountbottle = d // b
        normalbottle = d - discountbottle
        price = (normalbottle * a) + (discountbottle * c)
        print(price)
