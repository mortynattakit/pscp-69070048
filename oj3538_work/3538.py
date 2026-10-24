"""This code will check whether the string is all paired or not"""
text = input()
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1

result = ""
for char, count in counts.items():
    if count % 2:
        result += char

if result:
    print(result)
else:
    print("fully paired")
