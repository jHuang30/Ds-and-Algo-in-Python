# You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

# Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.


# Example 1:


# Input: root = [1, 0, 1, 0, 1, 0, 1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:

# Input: root = [0]
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
# Example 4:

# Input: root = [1, 1]
# Output: 3

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, current):
            if not root.left and not root.right:
                current += str(root.val)
                self.res += int(current, 2)
                return
            current += str(root.val)
            if root.left:
                dfs(root.left, current)
            if root.right:
                dfs(root.right, current)

        dfs(root, '')
        return self.res

# using binary calculation
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, current):
            if not root.left and not root.right:
                current = current * 2 + root.val
                self.res += current
                return
            current = current * 2 + root.val
            if root.left:
                dfs(root.left, current)
            if root.right:
                dfs(root.right, current)

        dfs(root, 0)
        return self.res
