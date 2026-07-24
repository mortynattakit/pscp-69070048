"""Temperature"""
temp = float(input())
deg = input()
degchange = input()

if deg == degchange:
    print(f"{(temp):.2f}")
elif deg == "C":
    if degchange == "K":
        print(f"{(temp + 273.15):.2f}")
    elif degchange == "R":
        print(f"{((temp + 273.15) * 9/5):.2f}")
    elif degchange == "F":
        print(f"{(temp * 9 / 5 + 32):.2f}")
elif deg == "K":
    degkc = temp - 273.15
    if degchange == "C":
        print(f"{(degkc):.2f}")
    elif degchange == "F":
        print(f"{(degkc * 9/5 + 32):.2f}")
    elif degchange == "R":
        print(f"{(temp * 9/5):.2f}")
elif deg == "F":
    degfc = (temp - 32) * 5 / 9
    if degchange == "C":
        print(f"{(degfc):.2f}")
    elif degchange == "K":
        print(f"{(degfc + 273.15):.2f}")
    elif degchange == "R":
        print(f"{((degfc + 273.15) * 9/5):.2f}")
elif deg == "R":
    degrc = (temp / 9 * 5) - 273.15
    if degchange == "C":
        print(f"{(degrc):.2f}")
    elif degchange == "K":
        print(f"{(degrc + 273.15):.2f}")
    elif degchange == "F":
        print(f"{(temp - 459.67):.2f}")
