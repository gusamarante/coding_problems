"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than
⌊n / 2⌋ times. You may assume that the majority element always
exists in the array.
"""


def majority_element(nums):

    count = {}

    for i in nums:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    return max(count, key=count.get)


print(majority_element([2, 2, 3, 2, 1]))

print(majority_element([2, 3, 3, 1, 4]))
