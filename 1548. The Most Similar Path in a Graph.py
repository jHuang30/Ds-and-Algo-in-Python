# We have n cities and m bi-directional roads where roads[i] = [ai, bi] connects city ai with city bi. Each city has a name consisting of exactly 3 upper-case English letters given in the string array names. Starting at any city x, you can reach any city y where y != x (i.e. the cities and the roads are forming an undirected connected graph).

# You will be given a string array targetPath. You should find a path in the graph of the same length and with the minimum edit distance to targetPath.

# You need to return the order of the nodes in the path with the minimum edit distance, The path should be of the same length of targetPath and should be valid (i.e. there should be a direct road between ans[i] and ans[i + 1]). If there are multiple answers return any one of them.

# The edit distance is defined as follows:



# Follow-up: If each node can be visited only once in the path, What should you change in your solution?

 

# Example 1:


# Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
# Output: [0,2,4,2]
# Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
# [0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance = 1 with targetPath.
# [0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance = 1 with targetPath.
# [0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance = 1 with targetPath.
# Example 2:


# Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
# Output: [0,1,0,1,0,1,0,1]
# Explanation: Any path in this graph has edit distance = 8 with targetPath.
# Example 3:



# Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
# Output: [3,4,5,4,3,2,1]
# Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.
# It's equivalent to ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
 

# Constraints:

# 2 <= n <= 100
# m == roads.length
# n - 1 <= m <= (n * (n - 1) / 2)
# 0 <= ai, bi <= n - 1
# ai != bi 
# The graph is guaranteed to be connected and each pair of nodes may have at most one direct road.
# names.length == n
# names[i].length == 3
# names[i] consists of upper-case English letters.
# There can be two cities with the same name.
# 1 <= targetPath.length <= 100
# targetPath[i].length == 3
# targetPath[i] consists of upper-case English letters.


# lte：

# class Solution:
#     def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
#         visited = [[0] * len(targetPath) for _ in range(n)]
#         best_candidate = [[0] * len(targetPath) for _ in range(n)]
#         dic = defaultdict(list)
#         for x, y in roads:
#             dic[x].append(y)
#             dic[y].append(x)
#         min_path = float('inf')
        
#         def dfs(name_idx, path_idx):
#             if visited[name_idx][path_idx]:
#                 return visited[name_idx][path_idx]
#             edit_dis = int(names[name_idx] != targetPath[path_idx])
#             if path_idx == len(targetPath) - 1:
#                 return edit_dis
#             min_dis = float('inf')
#             for neighbor in dic[name_idx]:
#                 next_cost = dfs(neighbor, path_idx + 1)
#                 if next_cost < min_dis:
#                     min_dis = next_cost
#                     best_candidate[name_idx][path_idx] = neighbor
#             visited[name_idx][path_idx] = min_dis + edit_dis
#             return edit_dis + min_dis
            
#         start = 0
#         res = []
#         for i in range(len(names)):
#             cost = dfs(i, 0)
#             if cost < min_path:
#                 min_path = cost
#                 start = i
#         while len(res) < len(targetPath):
#             res.append(start)
#             start = best_candidate[start][len(res) - 1]
#         return res
        
            
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        dic = defaultdict(list)
        for x, y in roads:
            dic[x].append(y)
            dic[y].append(x)
        target_len = len(targetPath)
        prev = [[0] * n for _ in range(target_len)]
        dp = [[target_len] * n for _ in range(target_len)]
        for i in range(n):
            dp[0][i] = (names[i] != targetPath[0])
        for i in range(1, target_len):
            for v in range(n):
                for u in dic[v]:
                    if dp[i - 1][u] < dp[i][v]:
                        dp[i][v] = dp[i - 1][u]
                        prev[i][v] = u
                dp[i][v] += (names[v] != targetPath[i])

        dis_min, res = float('inf'), [0]
        for i in range(n):
            if dp[-1][i] < dis_min:
                dis_min = dp[-1][i]
                res[0] = i
        for i in range(target_len - 1, 0, -1):
            res.append(prev[i][res[-1]])
        return res[::-1]