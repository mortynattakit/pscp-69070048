"""This code counts letter from the string user inputs"""
text = input()
count = 0
for i in text:
    if i in "aeiou":
        count += 1
print(count)
