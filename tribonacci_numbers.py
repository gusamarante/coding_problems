"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


def tribonacci(n):

    memo = {}

    def trib(i):

        if i == 0:
            return 0
        if i == 1 or i == 2:
            return 1
        if i not in memo:
            memo[i] = trib(i - 1) + trib(i - 2) + trib(i - 3)

        return memo[i]

    return trib(n)


print(tribonacci(25))
