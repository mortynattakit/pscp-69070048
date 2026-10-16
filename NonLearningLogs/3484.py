"""This code reports broken tiles and their total fine"""
num, price = input().split()
num = int(num)
price = float(price)
counts = [0] * num
points = [0] * num
for _ in range(num):
    row = list(map(int, input().split()))
    count = 0
    for j in range(num):
        if row[j]:
            count += 1
            counts[j] += 1
        points[j] += row[j]
    print(*row, count, sum(row))
print(*counts)
print(*points)
total = sum(points)
print(sum(counts), total, f"{total * price:.2f}")
