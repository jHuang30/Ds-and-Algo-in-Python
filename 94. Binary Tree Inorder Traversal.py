# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Example 1:


# Input: root = [1, null, 2, 3]
# Output: [1, 3, 2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:


# Input: root = [1, 2]
# Output: [2, 1]
# Example 5:


# Input: root = [1, null, 2]
# Output: [1, 2]


# Constraints:

# The number of nodes in the tree is in the range[0, 100].
# -100 <= Node.val <= 100

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)

        dfs(root)
        return self.res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
