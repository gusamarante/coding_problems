"""
Leetcode 114 - Longest Common Subsequence

Given two strings text1 and text2, return the length of their
longest common subsequence. If there is no common subsequence,
return 0.

A subsequence of a string is a new string generated from the
original string with some characters (can be none) deleted without
changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common
to both strings.
"""
from timeit import timeit
from functools import lru_cache


@lru_cache(maxsize=None)
def lcs(text1, text2):

    n1 = len(text1)
    n2 = len(text2)

    # Base Case
    if n1 == 0 or n2 == 0:
        return 0

    # Find the first commom letter (fcl)
    fcl = text2.find(text1[0])

    # first letter of text1 not in text2
    if fcl == -1:
        return lcs(text1[1:], text2)

    else:
        # Assume the 'fcl' is part of the solution
        case1 = 1 + lcs(text1[1:], text2[fcl + 1:])

        # Assume the 'fcl' is NOT part of the solution
        case2 = lcs(text1[1:], text2)

        return max(case1, case2)


# Example 1 - output should be 5
t1 = 'actgattag'
t2 = 'gtgtgatcg'

# Example 2 - output should be 10
# t1 = 'aaaaaaaaaaaaaaaaaaaaaaaaa'
# t2 = 'aaaaaaaaaa'

print(lcs(t1, t2))

tries = 10
print(timeit('lcs(t1, t2)', globals=globals(), number=tries) / tries)
