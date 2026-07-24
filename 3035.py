"""This code will output whether the eye position is in/on or outside of the circle"""
import math
inp = input().split(" ")
r = int(inp[0])
x = int(inp[1])
y = int(inp[2])

distance = math.dist((0,0),(x,y))
if distance > r:
    print("OUT")
elif distance == r:
    print("ON")
elif distance < r:
    print("IN")
