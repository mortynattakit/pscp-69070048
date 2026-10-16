"""This code lists cats and foxes in number order"""
import ast

num = int(input())
animals = {}
for _ in range(num):
    animals.update(ast.literal_eval(input()))
if "Garfield" not in animals and "Cat01" not in animals.values():
    animals["Garfield"] = "Cat01"
if "Fubuki" not in animals and "Fox01" not in animals.values():
    animals["Fubuki"] = "Fox01"
cats = []
foxes = []
for name, label in animals.items():
    item = (int(label[3:]), name, label)
    if label.startswith("Cat"):
        cats.append(item)
    else:
        foxes.append(item)
print("Cat :", len(cats))
print("Fox :", len(foxes))
for _, name, label in sorted(cats) + sorted(foxes):
    print(name, ":", label)
