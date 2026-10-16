"""This code counts letters in lowercase then uppercase order"""
text = input()
for char in "abcdefghijklmnopqrstuvwxyz":
    for letter in (char, char.upper()):
        count = text.count(letter)
        if count:
            print(letter, "=", count)
