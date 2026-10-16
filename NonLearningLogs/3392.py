"""This code stores three numbers and shows them in different orders"""
nums = [0] * 50
for i in range(3):
    nums[i] = int(input())
    print(f"Input number {i + 1} stored.")

while True:
    menu = int(input())
    if not menu:
        break
    if menu == 1:
        print("Original order:", *nums[:3])
    elif menu == 2:
        print("Descending order:", *sorted(nums[:3], reverse=True))
    elif menu == 3:
        print("Ascending order:", *sorted(nums[:3]))
