"""This code finds the lower and upper resistance from color bands"""
colors = "Black Brown Red Orange Yellow Green Blue Purple Grey White".split()
multipliers = {}
for i, color in enumerate(colors[:8]):
    multipliers[color] = 10 ** i
multipliers.update({"Gold": 0.1, "Silver": 0.01})
tolerance = {
    "Brown": 1, "Red": 2, "Green": 0.5, "Blue": 0.25,
    "Purple": 0.1, "Grey": 0.05, "Gold": 5, "Silver": 10
}
first = input()
second = input()
third = input()
fourth = input()

if (first not in colors or second not in colors
        or third not in multipliers or fourth not in tolerance):
    print("Error")
else:
    value = colors.index(first) * 10 + colors.index(second)
    value *= multipliers[third]
    change = value * tolerance[fourth] / 100
    print(f"{value - change:.4f}")
    print(f"{value + change:.4f}")
