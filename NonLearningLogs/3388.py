"""This code delete 113's from num text"""
num = input()
while True:
    if not "113" in num:
        break
    for i in range(len(num)):
        if i + 2 <= len(num) and (num[i:i+3] == "113"):
            num = num[:i] + num[i+3:]
print(num)
