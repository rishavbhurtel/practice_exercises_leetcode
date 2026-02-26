def getAverages(nums, k):
    if k == 0:
        return nums
    prefix_sum = [nums[0]]
    if len(nums) < k:
        avg = []
        for i in range(len(nums)):
            avg.append(-1)
        return avg
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[-1])
        print("prefix sum", prefix_sum)
    left = k
    right = (len(nums) - 1) - 3
    output = []
    curr = -1
    for i in range(len(nums)):
        print(i)
        if i < k or i > len(nums) - 1 - k:
            output.append(-1)
            print(output)
        else:
            if curr > -1:
                print(prefix_sum[i + k])
                print(prefix_sum[curr])
                output.append(
                    int((prefix_sum[i + k] - prefix_sum[curr]) / ((k * 2) + 1))
                )
                curr += 1
                print(output)
            else:
                print(prefix_sum[i + k])
                output.append(int((prefix_sum[i + k]) / ((k * 2) + 1)))
                curr += 1
                print(output)
    return output


nums = [3, 3]
k = 3
yo = getAverages(nums, k)
print(yo)
