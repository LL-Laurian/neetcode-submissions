"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        if node:
            new_head = Node(node.val)
        else:
            return

        def dfs(cur_node, cloned_node):
            print(cur_node.val)
            if cur_node.val in seen or not cur_node.neighbors:
                return

            seen[cur_node.val] = cloned_node
            for nei in cur_node.neighbors:
                if nei.val not in seen:
                    tmp = Node(nei.val)
                    dfs(nei, tmp)
                    cloned_node.neighbors.append(tmp)
                else:
                    cloned_node.neighbors.append(seen[nei.val])

        dfs(node, new_head)
        return new_head
                    