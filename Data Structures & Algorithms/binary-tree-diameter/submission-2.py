# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(head) -> tuple:
            if not head:
                return (0,0)
            left, l1 = dfs(head.left)
            right, l2 = dfs(head.right)

            longest = max(l1, l2, left+right)

            return (max(left, right) + 1, longest)

        return dfs(root)[1]
