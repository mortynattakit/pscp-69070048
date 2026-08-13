"""This code checks whether the numbers are the same or all different or neither"""
def main():
    """All the code here"""
    a = input()
    b = input()
    c = input()
    if a == b and b == c:
        print("all the same")
    elif a != b and b != c and a!= c:
        print("all different")
    else:
        print("neither")
main()
