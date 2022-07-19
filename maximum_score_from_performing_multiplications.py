"""
LeetCode 1770
You are given two integer arrays nums and multipliers of size n and m respectively,
where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations.
On the ith operation (1-indexed), you will:
- Choose one integer x from either the start or the end of the array nums.
- Add multipliers[i] * x to your score.
- Remove x from the array nums.

Return the maximum score after performing m operations.

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
"""


# My solution
def max_score(nums, multipliers):

    n, m = len(nums), len(multipliers)

    memo = {}

    def dp(i, left):
        if i == m:
            return 0

        if (i, left) not in memo:
            mult = multipliers[i]
            right = n - 1 - (i - left)
            memo[(i, left)] = max(mult * nums[left] + dp(i + 1, left + 1), mult * nums[right] + dp(i + 1, left))

        return memo[(i, left)]

    return dp(0, 0)


# print(max_score([1, 2, 3], [3, 2, 1]))
print(max_score([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))