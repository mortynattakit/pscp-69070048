"""This code will calculate ticket price"""
age, day = input().split()
age = int(age)
price = 0
if age < 5:
    price = 0
elif 5 <= age <= 18:
    price = 100
elif age > 18:
    price = 150

if day == "Wed":
    price /= 2
print(int(price))
