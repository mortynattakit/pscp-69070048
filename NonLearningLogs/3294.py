"""This code will calculate hour and minute"""
numofperiod = int(input())
period = int(input())
hour = (numofperiod * period) // 60
minute = (numofperiod * period) % 60
if not period or not numofperiod:
    print("No teaching")
else:
    print(f"{hour} hours" if hour > 0 else "", end="")
    print(" " if hour > 0 and minute > 0 else "", end="")
    print(f"{minute} minute" if minute > 0 else "")
