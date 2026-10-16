"""This code finds the most bridges crossed at once"""
length, num = map(int, input().split())
counts = [0] * length
for _ in range(num):
    start, end = map(int, input().split())
    for i in range(start, end):
        counts[i] += 1
print(max(counts))
