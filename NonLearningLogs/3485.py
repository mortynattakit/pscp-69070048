"""This code finds codes that appear once"""
num = int(input())
codes = list(map(int, input().split()))
counts = {}
for i in range(num):
    code = codes[i]
    counts[code] = counts.get(code, 0) + 1
result = []
for code, count in counts.items():
    if count == 1:
        result.append(code)
print(*sorted(result))
