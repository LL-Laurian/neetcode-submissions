# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        found = False

        def dfs(head, k):
            nonlocal res, found

            if not head or found:
                return 0
            
            left_size= dfs(head.left, k)

            right_size = 0

            if left_size +1 == k and not found:
                res = head.val
                found = True

            elif left_size +1 < k:
                right_size= dfs(head.right,k-(left_size+1))
            else:
                right_size= dfs(head.right,k) 
            
            return left_size + right_size + 1
        
        dfs(root, k)
        return res

            


            