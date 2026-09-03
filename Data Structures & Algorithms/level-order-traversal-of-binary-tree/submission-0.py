# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res =[]

        def dfs(head, depth):
            if not head:
                return None

            
            if len(res) <= depth:
                res.append([head.val])
            else:
                res[depth].append(head.val)

            dfs(head.left, depth+1)
            dfs(head.right, depth+1)
        
        dfs(root, 0)
        return res