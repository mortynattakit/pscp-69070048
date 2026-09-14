"""This code do caesar cipher."""
text = input()
shift = int(input())
newtxtascii = [((ord(char)-97 + shift) % 26) + 97 for char in text]
newtxt = ""
for i in newtxtascii:
    newtxt += chr(i)
print(newtxt)
