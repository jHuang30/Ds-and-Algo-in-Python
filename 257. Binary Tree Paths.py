# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []

        def dfs(root, current):
            if not root.left and not root.right:
                current += str(root.val)
                self.res.append(current)
                return
            current += str(root.val) + '->'

            if root.left:
                dfs(root.left, current)
            if root.right:
                dfs(root.right, current)

        dfs(root, '')
        return self.res


# better:

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []

        def dfs(root, current):
            if not root.left and not root.right:
                self.res.append(current + str(root.val))
            if root.left:
                dfs(root.left, current + str(root.val) + '->')
            if root.right:
                dfs(root.right, current + str(root.val) + '->')

        dfs(root, '')
        return self.res
