# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

# Example 1:

# Input: 
# grid = 
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]], 
# k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10. 
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# Example 2:

# Input: 
# grid = 
# [[0,1,1],
#  [1,1,1],
#  [1,0,0]], 
# k = 1
# Output: -1
# Explanation: 
# We need to eliminate at least two obstacles to find such a walk.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m - 1][n - 1] == 0


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k > m - 1 + n - 1:
            return m - 1 + n - 1
        queue = [[0, 0, k, 0]]
        visited = {}
        while queue:
            [x, y, remaining, steps] = queue.pop(0)
            key = f'{x}, {y}, {remaining}'
            if x >= m or x < 0 or y < 0 or y >= n or remaining < 0 or key in visited:
                continue
            if x == m - 1 and y == n - 1:
                return steps
            visited[key] = True
            queue.append([x + 1, y, remaining - grid[x][y], steps + 1])
            queue.append([x - 1, y, remaining - grid[x][y], steps + 1])
            queue.append([x, y + 1, remaining - grid[x][y], steps + 1])
            queue.append([x, y - 1, remaining - grid[x][y], steps + 1])
            
        return -1