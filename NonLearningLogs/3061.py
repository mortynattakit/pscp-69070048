"""This code calculates the score, prints the score and whether the user passes or not"""
score1 = int(input())
score2 = int(input())
total = score1 + score2
print(total)
print("pass" if total>=50 else "fail")
