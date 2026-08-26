"""this code will calculate how much tax each car owner has to pay"""
ad = int(input())
cc = int(input())
prices = []
taxprice = [[1250,1400,2000],[1100,1300,1700],[1000,1200,1500]]
if ad <= 1990:
    prices = taxprice[0]
elif ad < 2000:
    prices = taxprice[1]
elif ad >= 2000:
    prices = taxprice[2]

if cc <= 1500:
    print(prices[0])
elif cc <= 2000:
    print(prices[1])
elif cc > 2000:
    print(prices[2])
