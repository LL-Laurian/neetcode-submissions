# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node1 = list1
        node2 = list2
        
        head = ListNode()
        cur_res = head

        while node1 and node2:
            #print("This Line", node1.val, node2.val)
            #print("This curr", cur_res.val, cur_res.next)
            if node1.val < node2.val:
                cur_res.next = ListNode(node1.val)
                node1 = node1.next
            
            else:
                cur_res.next = ListNode(node2.val)
                node2 = node2.next
            
            cur_res = cur_res.next
        
        while node1:
            cur_res.next = ListNode(node1.val)
            node1 = node1.next
            cur_res = cur_res.next

        while node2:
            cur_res.next = ListNode(node2.val)
            node2 = node2.next
            cur_res = cur_res.next
        
        return head.next

