"""This code sorts points by their sum and then height"""
tests = int(input())
for _ in range(tests):
    num = int(input())
    points = []
    for _ in range(num):
        x, y = map(int, input().split())
        points.append((x + y, -y, x, y))
    points.sort()
    for point in points:
        print(point[2], point[3])
