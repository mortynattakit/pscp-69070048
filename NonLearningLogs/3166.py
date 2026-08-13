"""This code avg the score user input and check if the user passes or not"""
num = int(input())
scores = [int(input()) for _ in range(num)]

avgscore = sum(scores) / num
print(f"{avgscore:.1f}")

if avgscore < 60 or min(scores) < 50:
    print("FAIL")
else:
    print("PASS")
