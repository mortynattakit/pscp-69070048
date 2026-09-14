"""This code will find the 3 or 4-digit pass for the user"""
import math
numofsecret = input()
sepnum = list(map(int, numofsecret))

DIGIT1 = "9" if sepnum[0] > 5 else "10" if sepnum[1] > 5 else "11" if sepnum[2] > 5 else \
         "12" if sepnum[3] > 5 else "14" if sepnum[4] > 5 else "13"

if numofsecret == numofsecret[::-1]:
    DIGIT2 = "1" if sepnum[0] + sepnum[4] > 5 else "2" if sepnum[1] * sepnum[3] > 5 else "0"
else:
    DIGIT2 = "1" if  sepnum[4] and sepnum[0] // sepnum[4] > 5 \
        else "2" if sepnum[1] - sepnum[4] > 5 else "0"

DIGIT3 = "1" if sum(sepnum) > 25 else \
         "2" if math.prod(sepnum) > 55 else "0"

print(DIGIT1 + DIGIT2 + DIGIT3)
