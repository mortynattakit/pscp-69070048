"""This code counts passengers who reach their bus stop"""
capacity = int(input())
num = int(input())
stops = {}
for _ in range(num):
    people = list(map(int, input().split()))
    stops[people[0]] = people[1:]

bus = [0] * (num + 1)
count = 0
onboard = 0
for i in range(1, num + 1):
    count += bus[i]
    onboard -= bus[i]
    for destination in stops[i]:
        if onboard == capacity:
            break
        if destination > i:
            bus[destination] += 1
            onboard += 1
print(count)
