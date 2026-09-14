"""This code will tell how many steps till the goal or if not will print -1"""
start, goal = map(int, input().split())
count = 0
while True:
    if start > 0:
        count += 1
        goal -= start
        if goal <= 0:
            print(count)
            break
        start -= 2

    else:
        print(-1)
        break
