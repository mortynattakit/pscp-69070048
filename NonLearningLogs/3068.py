"""this code check whether the year is a leap year or not"""
year = int(input())
if (year <= 1582 and not year % 4) or not year % 400 or (not year % 4 and year % 100):
    print("yes")
else:
    print("no")
