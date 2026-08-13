"""This code checks whether the substance is solid, liquid or gas"""
temp = int(input())
degree = input().lower()


if (degree == 'c' and temp >= 100) or (degree == 'f' and temp >= 212):
    print("gas")
elif (degree == 'c' and 0 < temp < 100) or (degree == 'f' and 32 < temp < 212):
    print("liquid")
elif (degree == 'c' and temp <= 0) or (degree == 'f' and temp <= 32):
    print("solid")
