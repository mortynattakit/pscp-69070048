"""This code finds the heavier pig in each pair and their total"""
num = int(input())
weights = list(map(int, input().split()))
heaviest = []
for i in range(num):
    heaviest.append(max(weights[i * 2], weights[i * 2 + 1]))
if num == 1:
    print(heaviest[0])
else:
    print(" + ".join(map(str, heaviest)), "=", sum(heaviest))
