"""This code will find how many u after b or if not then add bu in text"""
s = input().strip()
t = s.upper()

if "BUU" in t:
    best = 0
    for i,_ in enumerate(t):
        if t[i] == "B":
            c = 0
            j = i + 1
            while j < len(t) and t[j] == "U":
                c += 1
                j += 1
            best = max(best, c)
    print("Yes", best)
elif "B" in t:
    k = t.index("B")
    print(s[:k + 1] + "U" * (len(s) - k - 1))
else:
    print(("BUU" * len(s))[:len(s)])
