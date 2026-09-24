"""LANDOKMAI 3299 664336"""
L, N = list(map(int, input().split()))
total = 0
k = 0

while total < N:
    k += 1
    for d in range((k - 1) * L + 1, k * L + 1):
        total += d
print(k)
