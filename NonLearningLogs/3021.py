"""this code will find if 2 circles are intersected to each other or not"""
import math
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

distfromorigin = math.dist((x1,y1), (x2,y2))
if r1 + r2 > distfromorigin:
    print("overlapping")
else:
    print("no overlapping")
