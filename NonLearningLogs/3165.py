"""walking in festivall"""
onedirection = input()
x = 0
y = 0
for ch in onedirection:
    match ch:
        case "N":
            y += 1
        case "S":
            y -= 1
        case "W":
            x -= 1
        case "E":
            x += 1
print(f"{x} {y} {abs(x) + abs(y)}")
