"""This code checks rabbit language"""
text = input().upper()
longest = 0
count = 0
wrong = -1
for i, char in enumerate(text):
    if char == "R":
        if i + 1 == len(text) or text[i + 1] != "A":
            wrong = min(i + 1, len(text) - 1)
            break
    elif char == "A":
        if not i or text[i - 1] not in "RA":
            wrong = i
            break
    elif char == "B":
        if i + 1 == len(text) or text[i + 1] not in "IT":
            wrong = min(i + 1, len(text) - 1)
            break
    elif char not in "IT":
        wrong = i
        break
    if char == "A":
        count += 1
        longest = max(longest, count)
    else:
        count = 0
if wrong != -1:
    print("no", wrong)
elif "R" not in text and "B" not in text:
    print("unknown", len(text))
else:
    print("yes", longest)
