"""Roll dice and guess"""
dice = int(input())
guess = int(input())
if 1 < dice > 6 or 1 < guess > 6:
    print("Invalid")
else:
    print("Correct!" if dice == guess else "Wrong!")
