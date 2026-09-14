"""This code wiil gift and thief"""
def main():
    """this code does the gift and theif"""
    N, K, T = map(int, input().split())

    if T == 1:
        print(1)
        return
    count = 1
    current = 1

    while True:
        nxt = (current - 1 + K) % N + 1
        if nxt == 1:
            break
        count += 1
        if nxt == T:
            break
        current = nxt
    print(count)

main()
