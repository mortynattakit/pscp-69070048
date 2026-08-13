"""Ink"""
import math
inkandperson = input().split(" ")
inkareapersec = int(inkandperson[0])
person = int(inkandperson[1])
times = []
for _ in range(person):
    coord = input().split(" ")
    x = int(coord[0])
    y = int(coord[1])
    time = math.ceil(((math.dist((0,0),(x,y))**2) * 3.1416) / inkareapersec)
    times.append(time)
for i in times:
    print(i)
