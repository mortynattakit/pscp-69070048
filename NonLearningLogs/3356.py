"""This code prints bus seats and marks the selected seat"""
seats = int(input())
rows = int(input())
selected = int(input())

for i in range(seats, 0, -1):
    line = []
    for j in range(rows):
        num = i + j * seats
        line.append("XX" if num == selected else f"{num:02d}")
    print(" ".join(line))
    if i > 1 and not (seats - i + 1) % 2:
        print()
