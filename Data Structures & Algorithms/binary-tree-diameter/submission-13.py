# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxWithHeight(self, root: Optional[TreeNode], max_c_2) -> (int, int):
       
       
        #base case: empty return 0
        if not root:
            return (0, max_c_2)
        #left, right; max (max, 1 + left + right)
        left_path, max_c_2 = self.maxWithHeight(root.left, max_c_2)
        right_path, max_c_2 = self.maxWithHeight(root.right, max_c_2)
        
        max_c_2 = max(max_c_2, 1 + left_path + right_path)
        print(1 + max(left_path, right_path), max_c_2)
        return (1 + max(left_path, right_path), max_c_2)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
       

        path_len, max_c_2 = self.maxWithHeight(root, 0)
             #return max of tuple from call
        
        return max(path_len, max_c_2) - 1
   