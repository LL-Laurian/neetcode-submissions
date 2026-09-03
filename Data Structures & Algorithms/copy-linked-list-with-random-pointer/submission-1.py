"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        random_node = {}
        new_Node = {}

        cur = head
        prev = None
        while cur:
            new_cur = Node(cur.val, None, None)
            new_Node[cur] = new_cur
            if cur in random_node:
                for node in random_node[cur]:
                    new_Node[node].random = new_cur

            if cur.random in new_Node:
                new_cur.random = new_Node[cur.random]

            if prev:
                prev.next = new_cur
            prev = new_cur

            if cur.random in random_node:
                random_node[cur.random].append(cur)
            else:
                random_node[cur.random] = [cur]
            cur = cur.next
        
        return new_Node[head]

        
