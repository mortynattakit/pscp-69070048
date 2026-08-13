"""This calculates the width and length of the paper gift thing"""

inp = input().split(" ")

r = float(inp[0])
h = float(inp[1])
gluedist = float(inp[2])
PI = 3.14

circle = 2 * PI * r + gluedist
area = h + 2 * r

print(f"{area:.2f} {circle:.2f}")
