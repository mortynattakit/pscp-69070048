"""this code will calculate how many times we have to tap the button to get the results we want"""
n = int(input())
count = 0

if n == 1:
    print("1")
else:
    for i in range(1,n+1):
        if i < 10:
            count += 2
        elif i < 100:
            count += 3
        elif i < 1000:
            count += 4
        elif i < 10000:
            count += 5
        elif i < 100000:
            count += 6
        elif i < 1000000:
            count += 7
    print(count)
