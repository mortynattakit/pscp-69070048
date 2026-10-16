"""This code finds the abnormal row and column in an array"""
area = []
for _ in range(5):
    area.append(list(map(int, input().split())))

row = -1
col = -1
for i in range(5):
    if sum(area[i]) % 2:
        row = i
    total = 0
    for j in range(5):
        total += area[j][i]
    if total % 2:
        col = i
print(row, col)
