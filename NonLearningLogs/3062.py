"""This code check the ticket costs between minors and adults"""
age = int(input())
sOrNot = input().lower()
if age < 18 or sOrNot == "s":
    print("20")
else:
    print("50")
