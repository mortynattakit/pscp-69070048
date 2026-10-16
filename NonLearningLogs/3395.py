"""This code finds the chair height each customer needs"""
num, count = map(int, input().split())
heights = list(map(int, input().split()))
customers = set(map(int, input().split()))
best = 0
for i, height in enumerate(heights, 1):
    if i in customers:
        print(max(0, best - height + 1))
    best = max(best, height)
