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
