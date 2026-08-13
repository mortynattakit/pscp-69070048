"""this code tell how many vowels that the user input"""
vowel = 0
num = int(input())
for character in range(num):
    character = input()
    if character in "AEIOU":
        vowel += 1
print(vowel)
