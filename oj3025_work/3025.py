"""Season"""
month = int(input())
day = int(input())

if 1 <= month <= 3:
    if day >= 21 and not month % 3:
        print("spring")
    else:
        print("winter")
elif 4 <= month <= 6:
    if day >= 21 and not month % 3:
        print("summer")
    else:
        print("spring")
elif 7 <= month <= 9:
    if day >= 21 and not month % 3:
        print("fall")
    else:
        print("summer")
elif 10 <= month <= 12:
    if day >= 21 and not month % 3:
        print("winter")
    else:
        print("fall")
