"""This code finds students listed in both groups"""
first_num = int(input())
second_num = int(input())
first = set()
second = set()
for _ in range(first_num):
    first.add(int(input()))
for _ in range(second_num):
    second.add(int(input()))
common = sorted(first & second, reverse=True)
if common:
    for student in common:
        print(student)
else:
    print("Nope")
