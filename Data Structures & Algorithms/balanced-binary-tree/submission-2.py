# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = True
        def dfs(root: Optional[TreeNode]) -> int:
                nonlocal res
                #base case none
                if not root:
                    return 0
                #post order left and right
                left = dfs(root.left)
                right = dfs(root.right)
                #compare -1 to 1
                if not (-1 <= (right - left) <= 1):
                    res = False
                    return 0
                #if false res =  False and return 0
                #else return 1 + max(left, right)
                return 1 + max(left, right)
        dfs(root)
        return res