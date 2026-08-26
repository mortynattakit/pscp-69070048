"""This code will calculate how many big and small bricks the user needs"""
smallbrick = int(input())
bigbrick = int(input())
goal = int(input())

bigused = min(bigbrick, goal // 5)
remainder = goal - bigused * 5
print(remainder if smallbrick >= remainder else -1)
