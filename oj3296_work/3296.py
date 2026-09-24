"""This code will find idk colors? rgb mixed 661612"""
red1,green1,blue1 = list(map(int, input().split()))
red2,green2,blue2 = list(map(int, input().split()))

print(f"{(red1+red2)//2} {(green1+green2)//2} {(blue1+blue2)//2}")
