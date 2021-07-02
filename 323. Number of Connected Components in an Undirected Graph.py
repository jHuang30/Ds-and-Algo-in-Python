# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = [i for i in range(n)]

        def find(x):
            nonlocal arr
            return x if arr[x] == x else find(arr[x])

        def union(x, y):
            nonlocal arr
            arr[find(x)] = find(y)

        for [x, y] in edges:
            union(x, y)

        return len([1 for idx, item in enumerate(arr) if idx == item])
