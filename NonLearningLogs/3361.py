"""This code counts car models that cannot be sold"""
num = int(input())
scores = []
for _ in range(num):
    scores.append(int(input().split()[1]))

best = 0
count = 0
for score in reversed(scores):
    if score < best:
        count += 1
    else:
        best = score
print(count)
