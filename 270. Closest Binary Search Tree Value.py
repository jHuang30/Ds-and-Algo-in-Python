# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

# Example 1:


# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return
            if abs(root.val - target) < abs(self.res - target):
                self.res = root.val
            if root.val < target:
                dfs(root.right)
            elif root.val > target:
                dfs(root.left)
            return self.res

        dfs(root)
        return self.res


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            # res = min(root.val, res, key = lambda x: abs(target - x))
            if abs(res - target) > abs(root.val - target):
                res = root.val
            root = root.left if root.val > target else root.right
        return res
