"""This code moves an explorer through a cave until reaching treasure"""
num = int(input())
area = list(map(int, input().split()))
commands = input()
position = area.index(1)
area[position] = 0
for direction in commands:
    nextpos = position + 1 if direction == "R" else position - 1
    if 0 <= nextpos < num:
        position = nextpos
    if area[position] == 2:
        break
area[position] = 1
print(*area)
