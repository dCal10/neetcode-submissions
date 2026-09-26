# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heights = {} #TreeNode to height in tree
        def height(root: Optional[TreeNode]) -> int:
            nonlocal heights
            if not root:
                return 0
            h = 1 + max(height(root.left), height(root.right))
            heights[root] = h
            return h
        # call height function
        height(root)
        def recuriveBalanced(root: Optional[TreeNode]) -> bool:
            if not root: return True            
            right = 0 if not root.right else heights[root.right]
            left = 0 if not root.left else heights[root.left]
            return recuriveBalanced(root.left) and recuriveBalanced(root.right) and abs(right - left) <= 1
        return recuriveBalanced(root)
        # if is balanced left and is baclnced right and if (heights[right] - heights[left]) <= 1
        