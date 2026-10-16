"""This code checks trash weight in each machine"""
num = int(input())
types = ["Plastic", "Can", "Glass"]
for _ in range(num):
    weights = list(map(float, input().split()))
    total = sum(weights)
    result = [f"{total:.1f}"]
    if total > 50:
        result.append("Overloaded")
    for i, weight in enumerate(weights):
        if weight > 20:
            result.append(f"Check Type {types[i]}")
    print(", ".join(result))
