"""this code will add/deduct points as many times as user inputs and return the result"""
num = int(input())
points = 0
for _ in range(num):
    arith = input()
    match arith:
        case "+":
            points += 10
        case "-":
            points -= 5
print(points)
