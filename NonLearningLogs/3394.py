"""This code counts students who receive a forwarded message"""
num, current = map(int, input().split())
friends = [0]
for _ in range(num):
    friends.append(int(input()))
seen = [False] * (num + 1)
count = 0
while current and not seen[current]:
    seen[current] = True
    count += 1
    current = friends[current]
print(count)
