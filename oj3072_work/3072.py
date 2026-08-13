"""This code checks how many each of the vowel in the sentence"""
a = 0
e = 0
ii = 0
o = 0
u = 0
array = input()
for i in array:
    if i in 'aA':
        a += 1
    elif i in 'eE':
        e += 1
    elif i in 'iI':
        ii += 1
    elif i in 'oO':
        o += 1
    elif i in 'uU':
        u += 1

if a > 0:
    print(f"a : {a}")
if e > 0:
    print(f"e : {e}")
if ii > 0:
    print(f"i : {ii}")
if o > 0:
    print(f"o : {o}")
if u > 0:
    print(f"u : {u}")
