# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        uniq_set = set()

        def dfs(i):
            nonlocal uniq_set
            for j in range(len(isConnected)):
                if (isConnected[i][j] and not j in uniq_set):
                    uniq_set.add(j)
                    dfs(j)

        for i in range(len(isConnected)):
            if not i in uniq_set:
                res += 1
                dfs(i)

        return res

# union find


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        arr = [x for x in range(len(isConnected))]

        def find(x):
            return x if arr[x] == x else find(arr[x])

        def union(x, y):
            arr[find(x)] = find(y)

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[0])):
                if isConnected[i][j]:
                    union(i, j)

        return len([1 for x, y in enumerate(arr) if x == y])
