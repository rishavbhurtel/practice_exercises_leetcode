"""Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
Example 1:

Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
Example 2:

Input: nums = [9,9,8,8]
Output: -1
Explanation: There is no number that occurs only once."""


def largestUniqueNumber(nums):
    nums_hash = {}
    ans = []
    for num in nums:
        nums_hash[num] = nums_hash.get(num, 0) + 1

    for k, v in nums_hash.items():
        if v == 1:
            ans.append(k)

    if not ans:
        return -1
    else:
        return sorted(ans)[-1]


# nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
nums = [9, 9, 8, 8]
yo = largestUniqueNumber(nums)
print(yo)
