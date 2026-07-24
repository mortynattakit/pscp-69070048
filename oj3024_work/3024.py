"""dsadasda"""
total = float(input())
maxnum = float(input())

minhighpos = max(0, (total - (2*maxnum)))

if maxnum - minhighpos > 2:
    print("Surprising")
elif maxnum - minhighpos <= 2:
    print("Not surprising")
2