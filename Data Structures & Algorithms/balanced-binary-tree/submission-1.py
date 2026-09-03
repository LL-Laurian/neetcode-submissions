# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calHeight(head):
            if not head:
                return (0, True)
            
            (l_h, l_isba) = calHeight(head.left)
            (r_h, r_isba) = calHeight(head.right)

            isba= True
            if abs(l_h - r_h) >1 or (not l_isba) or (not r_isba):
                print("here")
                isba = False

            return (max(l_h, r_h)+1, isba)
        
        _, isba = calHeight(root)
        return isba
            

        