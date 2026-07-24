"""dist"""
import math
one = input().split(" ")
x1 = int(one[0])
y1 = int(one[1])
z1 = int(one[2])

dos = input().split(" ")
x2 = int(dos[0])
y2 = int(dos[1])
z2 = int(dos[2])

print(f"{(math.sqrt(((x1-x2)**2) + ((y1-y2)**2) + ((z1-z2)**2))):.2f}")
