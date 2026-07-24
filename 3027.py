"""กระต่ายน้อยล้อมรั้วลวดหนาม"""
inp = input().split(" ")
width = int(inp[0])
length = int(inp[1])
floor = int(inp[2])
price = int(input())

total = ((width * 2) + (length * 2)) * floor
print(total)
print(total * price)
