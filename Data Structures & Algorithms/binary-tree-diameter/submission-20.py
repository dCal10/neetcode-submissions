# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #height function hat returns height of thing
        #nonlocal max that keeps storing the largest left + right + 1
        #return max of height and nonlocal max
        maximum = 0
        def height(root: Optional[TreeNode]):
            nonlocal maximum
            if not root:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)
            maximum = max(maximum, 1 + lheight + rheight)
            return 1 + max(lheight, rheight)
        depth = height(root)
        print(depth)
        return (max(maximum, depth) - 1)
        