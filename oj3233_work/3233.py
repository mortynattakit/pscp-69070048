"""THis code will if else prize of the lottery"""
winletter, winnum = input().split()
letter, num = input().split()

if letter == winletter and num == winnum:
    print(1000000)
elif num == winnum:
    print(100000)
elif letter == winletter and num[-3:] == winnum[-3:]:
    print(2000)
elif letter == winletter and num[-2:] == winnum[-2:]:
    print(1000)
elif num[-3:] == winnum[-3:]:
    print(200)
elif num[-2:] == winnum[-2:]:
    print(100)
elif letter == winletter:
    print(20)
else:
    print(0)
