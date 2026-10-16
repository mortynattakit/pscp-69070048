"""This code shortens consecutive numbers into ranges"""
nums = []
while True:
    num = int(input())
    if num == -1:
        break
    nums.append(num)
result = []
if nums:
    start = nums[0]
    end = start
    for num in nums[1:] + [-1]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")
            start = num
            end = num
print(", ".join(result))
