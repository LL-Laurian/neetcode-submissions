# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        head = root
        smaller = min(p.val, q.val)
        larger = max(p.val, q.val)
        while head:
            if (head.val == p.val or head.val == q.val) or (head.val <= larger and 
                head.val >= smaller):
                return head
            
            elif (head.val >= larger):
                head = head.left
            

            elif (head.val <= smaller):
                head = head.right
            
            else:
                print(head.val, p.val, q.val)
                return None
