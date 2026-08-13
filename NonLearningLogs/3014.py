"""This calculates how many bottles of milk can a customer buy with promotion"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

bottles = d // a
total = bottles

if b:
    caps = bottles
    while caps >= b:
        exchanged = (caps // b) * c
        caps = caps % b + exchanged
        total += exchanged

print(total)
