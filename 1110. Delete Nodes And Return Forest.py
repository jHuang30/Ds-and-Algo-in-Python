# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
 

# Constraints:

# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        delete_set = set(to_delete)
        queue = [[root, False]]
        while queue:
            current, parent = queue.pop(0)
            if not parent and current.val not in delete_set:
                res.append(current)
            if current.left:
                queue.append([current.left, current.val not in delete_set])
                if current.left.val in delete_set:
                    current.left = None
            if current.right:
                queue.append([current.right, current.val not in delete_set])
                if current.right.val in delete_set:
                    current.right = None

        return res


# dfs

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        delete_set = set(to_delete)

        def dfs(root, hasParent):
            if not root:
                return None
            if root.val not in delete_set and not hasParent:
                res.append(root)
            root.left = dfs(root.left, root.val not in delete_set)
            root.right = dfs(root.right, root.val not in delete_set)
            return None if (root.val in delete_set) else root

        dfs(root, False)
        return res
