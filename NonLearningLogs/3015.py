"""Pro"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())

free = x-y
total = z * a

people = total - ((z//x) * free * a)
print(people)
