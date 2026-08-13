"""add the max number till the user satisfy"""
num = int(input())
maxnum = []
for _ in range(num):
    a = int(input())
    b = int(input())
    maxnum.append(max(a,b))
if len(maxnum) == 1:
    print(maxnum[0])
else:
    print(" + ".join(map(str, maxnum)) + " = " + str(sum(maxnum)))
