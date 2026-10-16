"""This code finds the shortest walk to install bulbs"""
num = int(input())
heights = []
for _ in range(num):
    heights.append(int(input()))
heights.sort()
distance = 0
total = 0
for height in heights:
    distance += height
    total += distance * 2
print(total)
