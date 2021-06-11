# Given the root of a Binary Search Tree(BST), return the minimum difference between the values of any two different nodes in the tree.


# Example 1:


# Input: root = [4, 2, 6, 1, 3]
# Output: 1
# Example 2:


# Input: root = [1, 0, 48, null, null, 12, 49]
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range[2, 100].
# 0 <= Node.val <= 105

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = float('inf')
        self.prev = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev != None:
                self.res = min(root.val - self.prev, self.res)
            self.prev = root.val
            dfs(root.right)
            return

        dfs(root)
        return self.res
