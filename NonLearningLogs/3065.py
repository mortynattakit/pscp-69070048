"""THis code prints roman number from 1 to 10"""
def main():
    """All code here"""
    num = int(input())
    roman = ['I','II','III','IV','V','VI','VII','VIII','IX']
    if 1 <= num <= 9:
        print(roman[num-1])
    elif num < 0:
        print("Error : Please input positive number")
    else:
        print("Error : Out of range")
main()
