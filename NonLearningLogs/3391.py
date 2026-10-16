"""This code totals magic coins and checks the fire bonus"""
num = int(input())
coins = [0, 0, 0]
for _ in range(num):
    values = list(map(int, input().split()))
    for i in range(3):
        coins[i] += max(values[i], values[i + 3])

print(f"Total: {sum(coins)}")
print(f"Fire: {coins[0]}")
print(f"Water: {coins[1]}")
print(f"Earth: {coins[2]}")
print("Bonus:", "YES" if coins[0] > coins[1] + coins[2] else "NO")
