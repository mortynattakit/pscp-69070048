"""This code counts runners who are not lapped by the winner"""
num, laps = map(int, input().split())
times = []
for _ in range(num):
    times.append(int(input()))

fastest = min(times)
count = 0
for time in times:
    if time * (laps - 1) < fastest * laps:
        count += 1
print(count)
