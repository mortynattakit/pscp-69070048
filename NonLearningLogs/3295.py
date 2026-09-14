"""This code will calculate bill price of electricity"""
unit = int(input())
if unit > 200:
    print(f"{(((((unit - 200) * 15) + 2030) * 1.07) + (unit / 2)):.1f}")
elif unit > 100:
    print(f"{(((((unit - 100) * 12) + 50 + 280 + 500) * 1.07) + (unit / 2)):.1f}")
elif unit > 50:
    print(f"{(((((unit - 50) * 10) + 50 + 280) * 1.07) + (unit / 2)):.1f}")
elif unit > 10:
    print(f"{(((((unit - 10) * 7) + 50) * 1.07) + (unit / 2)):.1f}")
else:
    print(f"{((unit * 5 * 1.07) + (unit / 2)):.1f}")
