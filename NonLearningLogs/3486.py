"""This code locates the target from shell distances"""
import math

num = int(input())
shots = []
for _ in range(num):
    shots.append(tuple(map(int, input().split())))
x, y, distance = shots[0]
found = False
for target_x in range(1001):
    remaining = distance ** 2 - (target_x - x) ** 2
    if remaining < 0:
        continue
    offset = math.isqrt(remaining)
    if offset ** 2 != remaining:
        continue
    for target_y in (y - offset, y + offset):
        if not 0 <= target_y <= 1000:
            continue
        valid = True
        for a, b, dist in shots:
            if (target_x - a) ** 2 + (target_y - b) ** 2 != dist ** 2:
                valid = False
                break
        if valid:
            print(target_x, target_y)
            found = True
            break
    if found:
        break
