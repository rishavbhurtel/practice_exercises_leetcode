def runningSum(nums):
    sum = [nums[0]]
    for i in range(1, len(nums)):
        sum.append(nums[i] + sum[-1])
    return sum


nums = [3, 1, 2, 10, 1]
runningSum(nums)
