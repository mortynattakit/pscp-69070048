"""สลับตัวเลข"""
num = int(input())
arith = input()

NUMSWAPPED = int(str(num)[::-1])
result = num * NUMSWAPPED if arith == "*" else num + NUMSWAPPED
print(f"{num} {arith} {NUMSWAPPED} = {result}")
