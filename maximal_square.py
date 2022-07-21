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

    def dp(mat):
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):

                if mat[i][j] == 0:
                    sqr1 = mat[:i][:j]
                    sqr2 = mat[:i][j + 1:]
                    sqr3 = mat[i + 1:][:j]
                    sqr4 = mat[i + 1:][j + 1:]
                    return max(dp(sqr1), dp(sqr2), dp(sqr3), dp(sqr4))

        return n * m

    return dp(matrix)