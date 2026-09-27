"""This code will calculate the fee of the delivery"""
start, finish = input().split()
weight = float(input())

if start == 'BKK' and finish == "CNX":
    print(f"{((weight*30) + 10):.2f}")
elif start == 'CNX' and finish == "UBP":
    print(f"{((weight*40) + 15):.2f}")
elif start == 'UBP' and finish == "BKK":
    print(f"{((weight*40) + 20):.2f}")
elif start == 'BKK' and finish == "PKT":
    print(f"{((weight*50) + 25):.2f}")
elif start == 'PKT' and finish == "CNX":
    print(f"{((weight*60) + 30):.2f}")
elif start == 'UBP' and finish == "PKT":
    print(f"{((weight*70) + 40):.2f}")
else:
    print("Error")
