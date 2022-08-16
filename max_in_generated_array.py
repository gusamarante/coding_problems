"""
You are given an integer n. A 0-indexed integer array nums
of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums
"""


# Brute force solution
def get_max_generated(n):
    array = [0] * (n + 1)
    array[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 0:
            array[i] = array[int(i/2)]
        else:
            array[i] = array[int(i / 2)] + array[int(i / 2) + 1]

    return max(array)


for jj in range(1, 278):
    print(jj, get_max_generated(jj))
