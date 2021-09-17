# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.

# abs(x) is defined as:

# x for x >= 0.
# -x for x < 0.
 

# Example 1:


# Input: points = [[1,2,3],[1,5,1],[3,1,1]]
# Output: 9
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
# You add 3 + 5 + 3 = 11 to your score.
# However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
# Your final score is 11 - 2 = 9.
# Example 2:


# Input: points = [[1,5],[2,3],[4,2]]
# Output: 11
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
# You add 5 + 3 + 4 = 12 to your score.
# However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
# Your final score is 12 - 1 = 11.
 

# Constraints:

# m == points.length
# n == points[r].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 0 <= points[r][c] <= 105

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [[0] * len(points[0]) for _ in range(len(points))]
        # dp[i][j] = points[i][j] + max(dp[i - 1][k] - |j - k|)
        # j >= k: points[i][j] + max(dp[i - 1][k] - j + k) -> points[i][j] - j + max(dp[i - 1][k] + k)
        # j < k:  points[i][j] + max(dp[i - 1][k] + j - k) -> points[i][j] + j + max(dp[i - 1][k] - k)
        for i in range(len(points[0])):
            dp[0][i] = points[0][i]
        
        for i in range(1, len(points)):
            left, right = [0] * len(points[0]), [0] * len(points[0])
            
            left[0] = dp[i - 1][0]
            for k in range(1, len(points[0])):
                left[k] = max(left[k - 1], dp[i - 1][k] + k)
                
            right[-1] = dp[i - 1][-1] - (len(points[0]) - 1)
            for k in range(len(points[0]) - 2, -1, -1):
                right[k] = max(right[k + 1], dp[i - 1][k] - k)
            
            for j in range(len(points[0])):
                dp[i][j] = max(left[j] - j, right[j] + j) + points[i][j]

        return max(dp[-1])