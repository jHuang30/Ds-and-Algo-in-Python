# Given the root of a binary tree, return the sum of all left leaves.


# Example 1:


# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:

# Input: root = [1]
# Output: 0


# Constraints:

# The number of nodes in the tree is in the range[1, 1000].
# -1000 <= Node.val <= 1000

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, left):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right and left:
                res += root.val
                return

            dfs(root.left, True)
            dfs(root.right, False)
        dfs(root, False)
        return res
