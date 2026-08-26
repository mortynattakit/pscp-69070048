"""This code will calculate how much bonus the person gets"""
employee, workexp, salary = input().split()
workexp = int(workexp)
salary = int(salary)
bonus = 0
if employee == "M":
    if workexp > 10:
        bonus = 1500 + (salary * 10/100)
    elif workexp > 5:
        bonus = 1500 + (salary * 8/100)
    elif workexp <= 5:
        bonus = 1500 + (salary * 6/100)
elif employee == "B":
    if workexp >= 10:
        bonus = 1000 + (salary * 7/100)
    elif workexp > 5:
        bonus = 1000 + (salary * 6/100)
    elif workexp <= 5:
        bonus = 1000 + (salary * 5/100)
elif employee == "G":
    if workexp > 10:
        bonus = 500 + (salary * 6/100)
    elif workexp > 5:
        bonus = 500 + (salary * 5/100)
    elif workexp <= 5:
        bonus = 500 + (salary * 4/100)
print(int(bonus))
