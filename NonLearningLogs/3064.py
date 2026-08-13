"""this code check whether whose birthday is earlier"""
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

fromnow1 = abs((2025 - y1)*365 + (31 - d1) + (12 - m1)*30)
fromnow2 = abs((2025 - y2) + (31 - d2) + (12 - m2))
if -7 <= fromnow1 - fromnow2 <= 7:
    print("0")
elif fromnow1 < fromnow2:
    print(1)
else:
    print(2)
