"""put rectangle in the box"""
W, L, M, N = map(int, input().split())

best = W * L
for A in range(M, N + 1):
    waste = (L % A) * (W % A)
    best = min(best, waste)
print(best)
