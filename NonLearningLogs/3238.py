"""This code make X Shape as large as the input says with demanded character"""
num,character = input().split()
num = int(num)

mid = num//2

for i in range(num):
    for j in range(num):
        if j in (i, num - 1 - i):
            if character == "#":
                print("#", end="")
            else:
                print(chr(ord(character) + abs(mid - i)), end="")
        else:
            print("-",end="")
    print()
