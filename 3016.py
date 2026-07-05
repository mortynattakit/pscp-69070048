"""pattern 7 9 3 1"""
poweredby = int(input())
if poweredby % 4 == 1:
    print("7")
elif poweredby % 4 == 2:
    print("9")
elif poweredby % 4 == 3:
    print("3")
elif not poweredby % 4:
    print("1")
