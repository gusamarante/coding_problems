"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""


def palindrome(x):

    if x < 0:
        return False

    xstr = str(x)
    for i in range(int(len(xstr)/2)):

        if xstr[i] != xstr[-(i + 1)]:
            return False

    return True


print(palindrome(121))
print(palindrome(1336331))
print(palindrome(123))
print(palindrome(-121))
