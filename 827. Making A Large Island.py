# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

 

# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.


# lte
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        
        def dfs(i, j, seen):
            nonlocal n
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in seen:
                return 0
            seen[(i,j)] = True
            return dfs(i + 1, j, seen) + dfs(i - 1, j, seen) + dfs(i, j + 1, seen) + dfs(i, j - 1, seen) + 1
            
        no_zero = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    no_zero = False
                    grid[i][j] = 1
                    res = max(res, dfs(i, j, {}))
                    grid[i][j] = 0
        return n * n if no_zero else res



# n**2 

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        idx_with_islands = {0: 0}
        island_index = 2
        
        def dfs(i, j, idx):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] == 0 or grid[i][j] > 1:
                return 0
            grid[i][j] = idx
            return dfs(i + 1, j, idx) + dfs(i - 1, j, idx) + dfs(i, j + 1, idx) + dfs(i, j - 1, idx) + 1
            
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    idx_with_islands[island_index] = dfs(i, j, island_index)
                    island_index += 1
                    
        
        res = max(idx_with_islands.values())
        for i in range(n):
            for j in range(n):
                ans = 0
                seen = {}
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                if grid[i][j] == 0:
                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] not in seen :
                            seen[grid[x][y]] = True
                            ans += idx_with_islands[grid[x][y]]
                res = max(res, ans + 1)
        return res