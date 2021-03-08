# You are given the root of a binary search tree(BST), where exactly two nodes of the tree were swapped by mistake.Recover the tree without changing its structure.

# Follow up: A solution using O(n) space is pretty straight forward.Could you devise a constant space solution ?



#     Example 1:


# Input: root = [1, 3, null, null, 2]
# Output: [3, 1, null, null, 2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
#     Example 2:


# Input: root = [3, 1, 4, null, null, 2]
# Output: [2, 1, 4, null, null, 3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


#     Constraints:

# The number of nodes in the tree is in the range[2, 1000].
# - 231 <= Node.val <= 231 - 1

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """     
        first = second = prev = None
        
        def findCandidates(root):
            nonlocal first, second, prev
            if not root:
                return 
            findCandidates(root.left)
            if prev and prev.val > root.val:
                second = root
                if not first:
                    first = prev
                else:
                    return 
            prev = root
            findCandidates(root.right)
            
        
        findCandidates(root)
        first.val, second.val = second.val, first.val