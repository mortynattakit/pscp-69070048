"""This code counts trees that are taller than their neighbors"""
num = int(input())
heights = [0] + list(map(int, input().split())) + [0]
count = 0
for i in range(1, num + 1):
    if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
        count += 1
print(count)
