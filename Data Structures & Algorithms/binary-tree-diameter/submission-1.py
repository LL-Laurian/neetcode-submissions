# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(head, longest) -> tuple:
            if not head:
                return (0, longest)
            left, l1 = dfs(head.left, longest)
            right, l2 = dfs(head.right, longest)

            longest = max(longest, l1, l2, left+right)

            return (max(left, right) + 1, longest)

        return dfs(root, 0)[1]
