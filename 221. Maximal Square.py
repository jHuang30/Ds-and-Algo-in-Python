# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


# Example 1:


# Input: matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
#     "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0", "1"], ["1", "0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

#2d
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0 or matrix[i][j] == "0":
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j] * dp[i][j])
                    
        return res

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0] * len(matrix[0])
        prev = 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = dp[j]
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    dp[j] = int(matrix[i][j])
                else:
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                res = max(res, dp[j] * dp[j])
                prev = temp
                
        return res

