"""THis code will find the least day to finish all work"""
num = int(input())
work = []
for i in range(num):
    work.append(int(input()))

long = 0
for i in work:
    if i > 18:
        long += 1
short = num - long

if long <= short + 1:
    print(num)
else:
    print(2 * long - 1)
