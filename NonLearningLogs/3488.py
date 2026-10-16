"""This code finds the longest time under the lights"""
num = int(input())
lights = [False] * 360
for _ in range(num):
    start, end = map(int, input().split())
    for i in range((end - start) % 360):
        lights[(start + i) % 360] = True
count = 0
best = 0
for light in lights * 2:
    if light:
        count += 1
        best = max(best, count)
    else:
        count = 0
print(min(best, 360))
