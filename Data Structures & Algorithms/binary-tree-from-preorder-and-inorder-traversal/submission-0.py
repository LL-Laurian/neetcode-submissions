# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        n = len(preorder)

        for i, val in enumerate(inorder):
            inorder_index[val] = i
        
        def rebuild(preordstart, preordend, inordstart, inordend):
            if preordstart >= preordend or inordstart >= inordend:
                return None

            rootNode = TreeNode(preorder[preordstart])
            
            root_inord = inorder_index[preorder[preordstart]]
            left_inordend = root_inord
            right_inordstart = root_inord+1

            left_tree_length = left_inordend - inordstart

            left_preordstart = preordstart + 1
            left_preordend = left_preordstart + left_tree_length

            right_preordstart = left_preordend

            left = rebuild(left_preordstart, left_preordend, inordstart, left_inordend)
            right = rebuild(right_preordstart, preordend, right_inordstart, inordend)

            rootNode.left, rootNode.right = left, right

            return rootNode
        
        return rebuild(0, n, 0, n)


