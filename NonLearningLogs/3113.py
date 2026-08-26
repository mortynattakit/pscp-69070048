"""This code will calculate the price of the ramen"""
size, flavor = input().split()
topping = input().split()

ramen = {
    "S": {"R":60,"T":80},
    "M": {"R":80,"T":100},
    "L": {"R":100,"T":120}
}
toppings = {
    "P": 15,
    "E": 10
}
if topping[0] == 'N':
    print(ramen[size][flavor])
else:
    print(ramen[size][flavor] + toppings[topping[0]]*int(topping[1]))
