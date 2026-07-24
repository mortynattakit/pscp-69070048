"""This code will outputs how many of each coin will the user gets based on the input"""
money = int(input())

print(f"10 = {money // 10}")
print(f"5 = {money % 10 // 5}")
print(f"2 = {money % 10 % 5 // 2}")
print(f"1 = {money % 10 % 5 % 2}")
