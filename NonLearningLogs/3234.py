"""This code wil print the start with the color input specified 
and then rgb the way till a certain input number"""
color, n = input().split()
n = int(n)

colors = ["Red", "Green", "Blue"]
start = {
    'R':0,
    "G":1,
    "B":2
}[color]

for i in range(n):
    print(colors[(start + i) % 3],end=" ")
