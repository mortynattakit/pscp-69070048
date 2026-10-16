"""This code calculates team scores"""
num, members = map(int, input().split())
if not 1 <= num <= 10 or not 1 <= members <= 20:
    print("Data Incorrect")
else:
    teams = []
    valid = True
    for _ in range(num):
        team = list(map(int, input().split()))
        teams.append(team)
        if len(team) != members:
            valid = False
        for score in team:
            if not 0 <= score <= 100:
                valid = False
    if not valid:
        print("Data Incorrect")
    else:
        total = 0
        for i, team in enumerate(teams, 1):
            total += sum(team)
            print(f"Team {i}: Average = {sum(team) / members:.2f}, "
                  f"Max = {max(team)}")
        print(f"Total Score of All Teams = {total}")
