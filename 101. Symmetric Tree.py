# Given the root of a binary tree, check whether it is a mirror of itself(i.e., symmetric around its center).


# Example 1:


# Input: root = [1, 2, 2, 3, 4, 4, 3]
# Output: true
# Example 2:


# Input: root = [1, 2, 2, null, 3, null, 3]
# Output: false


# Constraints:

# The number of nodes in the tree is in the range[1, 1000].
# -100 <= Node.val <= 100


# Follow up: Could you solve it both recursively and iteratively?

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True

# dfs:


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        return dfs(root, root)
