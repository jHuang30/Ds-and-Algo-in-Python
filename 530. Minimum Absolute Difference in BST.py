# 530. Minimum Absolute Difference in BST
# Easy

# 1311

# 93

# Add to List

# Share
# Given the root of a Binary Search Tree(BST), return the minimum absolute difference between the values of any two different nodes in the tree.


# Example 1:


# Input: root = [4, 2, 6, 1, 3]
# Output: 1
# Example 2:


# Input: root = [1, 0, 48, null, null, 12, 49]
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range[2, 104].
# 0 <= Node.val <= 105


# Note: This question is the same as 783: https: // leetcode.com/problems/minimum-distance-between-bst-nodes/
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = float("inf")
        self.prev = None

        def dfs(root):
            if not root:
                return self.res
            dfs(root.left)
            if self.prev != None:
                self.res = min(self.res, root.val - self.prev)
            self.prev = root.val
            dfs(root.right)
            return self.res

        dfs(root)
        return self.res
