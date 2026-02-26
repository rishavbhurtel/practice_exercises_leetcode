def sortedSquares(nums):
    i = 0
    j = len(nums) - 1
    output = [0] * len(nums)
    for k in range(len(nums) - 1, -1, -1):
        if nums[i] * nums[i] < nums[j] * nums[j]:
            output[k] = nums[j] * nums[j]
            print("j", j)
            j -= 1
            print(output)

        else:
            output[k] = nums[i] * nums[i]
            print("i", i)
            i += 1
            print(output)

    return output


nums = [-7, -3, 2, 3, 11]
sortedSquares(nums)
