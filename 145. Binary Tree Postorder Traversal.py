# Given the root of a binary tree, return the postorder traversal of its nodes' values.


# Example 1:


# Input: root = [1, null, 2, 3]
# Output: [3, 2, 1]
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
# Output: [2, 1]


# Constraints:

# The number of the nodes in the tree is in the range[0, 100].
# -100 <= Node.val <= 100

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            self.res.append(root.val)

        dfs(root)
        return self.res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            current = stack.pop()
            res.insert(0, current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return res
