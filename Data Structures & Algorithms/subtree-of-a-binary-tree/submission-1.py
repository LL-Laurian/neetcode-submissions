# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(r , subr, check):
            if not r and not subr:
                return True
            
            if (not r and subr) or (not subr and r):
                return False

            
            if r.val == subr.val:
                left = dfs(r.left, subr.left, True)
                right = dfs(r.right, subr.right, True)

                if left and right: return True
            
            elif check:
                return False
            
            left = dfs(r.left, subr, False)
            right = dfs(r.right, subr, False)

            return left or right
            
        return dfs(root, subRoot, False)
