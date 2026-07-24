"""This calculates how many bottles of milk can a customer buy with promotion"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if not b:
    print(d // a)
else:
    totalbottle = (d // a) + (((d // a) // b) * c)
    dummy = ((d // a) // b) * c
    while True:
        if dummy >= b:
            dummy = (dummy % b) + ((dummy // b) * c)
            totalbottle += dummy
        elif dummy < b:
            break

    print(totalbottle)
