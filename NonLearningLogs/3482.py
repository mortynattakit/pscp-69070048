"""This code fights demons until five are defeated"""
demons = [("Spider Demon", 1), ("Swamp Demon", 2),
          ("Arrow Demon", 1), ("Hand Demon", 2),
          ("Drum Demon", 3), ("Mugen Train", 2), ("Upper Moon", 3)]
count = 0
total = 0
i = 0
while count < 5:
    name, target = demons[i]
    print(name)
    for _ in range(2):
        num = int(input())
        total += 1
        if num == target:
            print("kill")
            count += 1
            break
    else:
        print("back")
        demons.append((name, target))
    i += 1
print(total)
