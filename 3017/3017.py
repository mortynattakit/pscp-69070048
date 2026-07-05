"""This code will prints the money and vat"""
total = int(input())
servicecharge = total / 10
servicecharge = max(servicecharge, 50)
servicecharge = min(servicecharge, 1000)

total += servicecharge
total += total / 100 * 7

print(f"{total:.2f}")
