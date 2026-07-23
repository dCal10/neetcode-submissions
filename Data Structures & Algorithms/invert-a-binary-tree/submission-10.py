# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        if not root:
            return None
        q.append(root)
        while q:
            #get current node
            node = q.popleft()

            #swap children
            temp = node.left
            node.left = node.right
            node.right = temp

            #add children to q if not none
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        # return root
        return root


