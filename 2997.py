"this code calculates who has more chance of winning"
ra = int(input())
rb = int(input())
competitor = input()
if competitor == "A":
    print(f"{(1/(1+(10**((rb-ra)/400)))):.2f}")
elif competitor == "B":
    print(f"{(1/(1+(10**((ra-rb)/400)))):.2f}")
