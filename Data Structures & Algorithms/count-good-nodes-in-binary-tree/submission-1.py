# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        cur_max = -101

        def traverse(r, cm):
            cur = 0

            if r.val >= cm:
                cur = 1

            if r.left is None and r.right is None:
                return cur
            
            else:
                new_max = max(r.val, cm)
                left, right = 0, 0
                if r.left is not None:
                    left = traverse(r.left, new_max)
                if r.right is not None:
                    right = traverse(r.right, new_max)

                
                return cur + left + right
        
        return traverse(root, cur_max)
