"""This code calculate if the user passes or not"""
assign = int(input())
midterm = int(input())
final = int(input())

if assign >= 5 and midterm >= 20 and final >= 25:
    print("pass")
else:
    print("fail")
