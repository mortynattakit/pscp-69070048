"""this code checks whether the input password for the safe is right"""
char = input()
digits = input()
if char == "H" and digits == "4567":
    print("safe unlocked")
elif digits == "4567" and char != "H":
    print("safe locked - change char")
elif digits != "4567" and char == "H":
    print("safe locked - change digit")
else:
    print("safe locked")
