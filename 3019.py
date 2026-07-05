"""This code check if the safe password is correct or not"""
letter = input()
digits = input()
if letter == "H" and digits == "4567":
    print("safe unlocked")
elif letter == "H":
    print("safe locked - change digit")
elif digits == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
