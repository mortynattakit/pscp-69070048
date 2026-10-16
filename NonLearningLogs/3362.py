"""This code makes a love charm from two names"""
name1 = input().lower()
name2 = input().lower()
text = ""
count = 0
longest = 0
current = 0
for i in range(max(len(name1), len(name2))):
    if name1[i % len(name1)] in "love" or name2[i % len(name2)] in "love":
        text += "w"
        count += 1
        current += 1
        longest = max(longest, current)
    else:
        text += "$"
        current = 0

if count % 2:
    text += str(longest)
elif "ww" not in text:
    text += "#"
print(text)
