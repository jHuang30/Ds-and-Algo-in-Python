# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
 

# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if (left == 0 or right == 0):
            return left + right + 1
        else:
            return min(left, right) + 1

# bfs


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [[root, 1]]
        while queue:
            [current, level] = queue.pop(0)
            if not current.left and not current.right:
                return level
            if current.left:
                queue.append([current.left, level + 1])
            if current.right:
                queue.append([current.right, level + 1])

        return level
