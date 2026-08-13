"""This code checks how many banknotes atm needs to print out for customer"""
money = int(input())
thou = money // 1000
fivehund = (money % 1000) // 500
hund = ((money % 1000) % 500) // 100

if money > 20000 or money % 100:
    print("ERROR")
else:
    if thou > 0:
        print(f"1000 = {thou}")
    if fivehund > 0:
        print(f"500 = {fivehund}")
    if hund > 0:
        print(f"100 = {hund}")
