def minStartValue(nums):
    min_val = total = 0
    for num in nums:
        total += num
        min_val = min(min_val, total)
    return -min_val + 1


nums = [2, 3, 5, -5, -1]
yo = minStartValue(nums)
print(yo)
