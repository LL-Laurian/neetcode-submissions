# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
            
        neigh = deque([(root,0)])
        predepth = -1

        while neigh:
            node, depth = neigh.popleft()
            if depth != predepth:
                res.append(node.val)
            if node.right: neigh.append((node.right, depth+1))
            if node.left: neigh.append((node.left, depth+1))
            predepth = depth


        return res