"""
Leetcode 221 - Maximal Square
Given an m x n binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return
its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Input: matrix = [["0"]]
Output: 0
"""


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    n = len(matrix)
    m = len(matrix[0])

    # size of square at i,j position in dp
    dp = [[0 for i in range(m)] for j in range(n)]
    side = 0

    for i in range(n):
        if dp[i][0] == 1:
            dp[i][0] = 1

    for j in range(1, m):
        if dp[0][j] == 1:
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 1:
                # dp[i][j] is the final answer,
                # the last block of the square in this case.
                from_up = dp[i - 1][j]
                from_right = dp[i][j - 1]
                from_dia = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(from_up, from_right, from_dia)
            side = max(side, dp[i][j])
    return side * side


mat = [[1, 0, 1, 0, 0],
       [1, 0, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 0, 0, 1, 0]]

print(maximalSquare(mat))
