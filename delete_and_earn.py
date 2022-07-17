"""
Leetcode 740
You are given an integer array nums. You want to maximize the number of points
you get by performing the following operation any number of times: Pick any
nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every
element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation
some number of times.
"""


def delete_and_earn(nums):
    points = {}
    memo = {}
    max_number = max(nums)

    for num in nums:
        if num not in points:
            points[num] = num
        else:
            points[num] += num

    def max_points(n):
        if n == 0:
            return 0
        elif n == 1:
            if 1 in points:
                return points[1]
            else:
                return 0
        else:
            try:
                gain = points[n]
            except KeyError:
                gain = 0

            if n not in memo:
                memo[n] = max(max_points(n - 1), max_points(n - 2) + gain)

            return memo[n]

    return max_points(max_number)


print(delete_and_earn([1, 1, 1, 2, 4, 5, 5, 5, 6]))
