"""This code finds three digit numbers from hints"""


def check(digit, compare, target):
    """Check a digit with the hint"""
    if compare == "==":
        return digit == target
    if compare == ">":
        return digit > target
    if compare == "<":
        return digit < target
    if compare == "<=":
        return digit <= target
    if compare == ">=":
        return digit >= target
    return digit != target


hints = []
for _ in range(3):
    sign, goal = input().split()
    hints.append((sign, int(goal)))

for num in range(1000):
    units = num % 10
    tens = num // 10 % 10
    hundreds = num // 100
    if (check(units, *hints[0]) and check(tens, *hints[1])
            and check(hundreds, *hints[2])):
        print(f"{num:03d}")
