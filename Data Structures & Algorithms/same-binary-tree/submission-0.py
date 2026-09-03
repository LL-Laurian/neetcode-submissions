# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(head1, head2):
            if not head1 and not head2:
                return True
            if (not head1 and head2) or (not head2 and head1):
                return False

            if head1.val != head2.val:
                return False

            left = dfs(head1.left, head2.left)
            right = dfs(head1.right, head2.right)

            return left and right
        
        return dfs(p,q)
        

        

        