"""This code compares which rabbit is the heaviest"""
num = int(input())
rabbit = {}
count = 0
for _ in range(num):
    key,value = map(str, input().split())
    value = int(value)
    if value > 15 :
        count += 1
    rabbit[key] = value
print(count)
print(max(rabbit, key=rabbit.get))
