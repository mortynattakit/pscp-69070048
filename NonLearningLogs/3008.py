'''This code prints heron of alexandria'''
import math as kanid
a = float(input())
b = float(input())
c = float(input())
s = (a+b+c)/2

print(f"{(kanid.sqrt(s*(s-a)*(s-b)*(s-c))):.3f}")
