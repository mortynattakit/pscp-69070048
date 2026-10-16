"""This code draws a square from a value in a tuple"""
texts = tuple(input().split())
text = input()
count = texts.count(text)
position = texts.index(text)
for _ in range(count):
    print(*[position] * count)
