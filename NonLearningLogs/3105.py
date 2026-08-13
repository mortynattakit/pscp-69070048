"""This code will calculate """
distance = int(input())
if not distance:
    print(0)
elif distance == 1:
    print(35)
elif 1 < distance <= 10:
    print(35 + ((distance-1) * 5))
elif distance > 10:
    print(80 + ((distance-10) * 8))
