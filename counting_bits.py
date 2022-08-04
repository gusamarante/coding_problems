"""
Given an integer n, return an array ans of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary
representation of i.


Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0 --> 0
1 --> 1 --> 1
2 --> 10 --> 1
3 --> 11 --> 2
4 --> 100 --> 1
5 --> 101 --> 2
6 --> 110 --> 2
7 --> 111 --> 3
8 --> 1000 --> 1
"""


def count_bits(n):

    res = [0]

    if n == 0:
        return res

    else:
        count = 1
        while len(res) < n + 1:

            new_res = [x + 1 for x in res]
            res = res + new_res

            count += 1

        return res[:n+1]


print(count_bits(8))
