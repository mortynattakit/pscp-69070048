"""This code finds numbers in set A that are not in set B"""
n = int(input())
m = int(input())
a = set()
b = set()
for _ in range(n):
    a.add(int(input()))
for _ in range(m):
    b.add(int(input()))
print(*sorted(a - b))
