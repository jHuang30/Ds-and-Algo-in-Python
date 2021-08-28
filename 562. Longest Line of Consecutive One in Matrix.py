# Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

# The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

# Example 1:


# Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# Output: 3
# Example 2:


# Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
# Output: 4
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        dp = [[[0 for _ in range(4)] for _ in range(len(mat[0]))] for _ in range(len(mat))]
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # left, up, dia, anti-dia
                if j == 0 and i == 0 or mat[i][j] == 0:
                    dp[i][j] = [mat[i][j], mat[i][j], mat[i][j], mat[i][j]]
                elif i == 0:
                    dp[i][j] = [dp[i][j - 1][0] + 1, 1, 1, 1]
                elif j == 0:
                    if j + 1 < len(mat[0]):
                        dp[i][j] = [1, dp[i - 1][j][1] + 1, 1, dp[i - 1][j + 1][3] + 1]
                    else:
                        dp[i][j] = dp[i][j] = [1, dp[i - 1][j][1] + 1, 1, 1]
                else:
                    if j + 1 < len(mat[0]):
                        dp[i][j] = [dp[i][j - 1][0] + 1, dp[i - 1][j][1] + 1, dp[i - 1][j - 1][2] + 1, dp[i - 1][j + 1][3] + 1]
                    else:
                        dp[i][j] = [dp[i][j - 1][0] + 1, dp[i - 1][j][1] + 1, dp[i - 1][j - 1][2] + 1, 0]
                res = max(res, max(dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3]))
        return res