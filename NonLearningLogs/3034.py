"""This code """
def main():
    """The code runs in this function"""
    N, K = map(int, input().split())
    Klist = [0] * K
    for _ in range(N):
        num = int(input())
        Klist[num-1] += 1

        if all(num >= 1 for num in Klist):
            Klist = [num - 1 for num in Klist]
    print(sum(Klist))
main()
