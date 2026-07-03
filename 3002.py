"""This code prints password for people that input in here"""
firstname = input()
lastname = input()
age = input()

if len(firstname) >= 5 and len(lastname) >= 5:
    print(firstname[0:2]+lastname[-1]+age[-1])
else:
    print(firstname[0]+age+lastname[-1])
