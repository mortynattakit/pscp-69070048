"""This code finds the least number of bowl stacks"""
num = int(input())
bowls = [0] * 301
for _ in range(num):
    size = int(input())
    bowls[size] += 1
print(max(bowls))
