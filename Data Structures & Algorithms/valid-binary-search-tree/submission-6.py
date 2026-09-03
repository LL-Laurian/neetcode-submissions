# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(head):
            if not head:
                return True, None, None
            
            left, leftmin, leftmax = isValid(head.left)
            right, rightmin, rightmax = isValid(head.right)

            left_ok = leftmax is None or leftmax < head.val
            right_ok = rightmin is None or head.val < rightmin

            subtree_min = leftmin if leftmin is not None else head.val
            subtree_max = rightmax if rightmax is not None else head.val

            return left and right and left_ok and right_ok, subtree_min, subtree_max
            
        return isValid(root)[0]
            