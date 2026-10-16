"""This code finds safe areas and rabbit infection risk"""
rows, cols = map(int, input().split())
x, y = map(int, input().split())
num = int(input())
area = [[0] * cols for _ in range(rows)]
for _ in range(num):
    r, c = map(int, input().split())
    for i in range(max(0, r - 2), min(rows, r + 3)):
        for j in range(max(0, c - 2), min(cols, c + 3)):
            distance = max(abs(i - r), abs(j - c))
            risk = [100, 60, 20][distance]
            area[i][j] = max(area[i][j], risk)

print(sum(row.count(0) for row in area))
print(f"{area[x][y]}%")
