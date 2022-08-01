"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


def is_subsequence(s, t):

    ns = len(s)
    nt = len(t)
    start = 0

    for i in range(ns):
        has_letter = False

        for j in range(start, nt):

            if s[i] == t[j]:
                has_letter = True
                start = j+1
                break

        if has_letter == True:
            pass
        else:
            return False

    return True


print(is_subsequence('acb', 'ahbdc'))
