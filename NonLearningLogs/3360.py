"""This code finds the two largest bread pieces"""
width, height, cols, rows = map(int, input().split())
x = [0] + list(map(int, input().split())) + [width]
y = [0] + list(map(int, input().split())) + [height]
widths = []
heights = []
for i in range(cols + 1):
    widths.append(x[i + 1] - x[i])
for i in range(rows + 1):
    heights.append(y[i + 1] - y[i])
widths.sort(reverse=True)
heights.sort(reverse=True)
biggest = widths[0] * heights[0]
second = max(widths[0] * heights[1], widths[1] * heights[0])
print(biggest, second)
