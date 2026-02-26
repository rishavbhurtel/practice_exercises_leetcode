def findMaxAverage(nums, k):
    sums = ans = 0
    for i in range(0, k):
        sums += nums[i]
    avg = sums / k
    ans = avg
    print(len(nums))
    print(k)
    for i in range(k, len(nums)):
        sums = sums + nums[i] - nums[i - k]
        avg = sums / k
        ans = max(avg, ans)
    print(ans)


nums = [0, 1, 1, 3, 3]
k = 4

findMaxAverage(nums, k)
