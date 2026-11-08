# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        def dfs(r: TreeNode) -> tuple[bool, bool]:
            nonlocal lca
            if not r:
                return (False, False)
            pFoundLeft, qFoundLeft = dfs(r.left)
            pFoundRight, qFoundRight = dfs(r.right)
            pFound = pFoundLeft or pFoundRight or r.val == p.val
            qFound = qFoundLeft or qFoundRight or r.val == q.val
            if pFound and qFound and not lca:
                lca = r
            return (pFound, qFound)
        dfs(root)
        return lca