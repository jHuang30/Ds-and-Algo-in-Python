// Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

// The distance between two nodes is the number of edges on the path from one to the other.



//     Example 1:


// Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 0
// Output: 3
// Explanation: There are 3 edges between 5 and 0: 5 - 3 - 1 - 0.
// Example 2:


// Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 7
// Output: 2
// Explanation: There are 2 edges between 5 and 7: 5 - 2 - 7.
// Example 3:


// Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 5
// Output: 0
// Explanation: The distance between a node and itself is 0.


// Constraints:

// The number of nodes in the tree is in the range[1, 104].
// 0 <= Node.val <= 109
// All Node.val are unique.
// p and q are values in the tree.

class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if (p == q): return 0
        
        def dfs(root, depth):
            if not root:
                return 0
            if p == root.val or q == root.val:
                left = dfs(root.left, 1)
                right = dfs(root.right, 1)
                if left or right:
                    return left or right
                else:
                    return depth
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
            if left and right:
                return left + right - 2 * depth
            return left + right
        
        return dfs(root, 0)