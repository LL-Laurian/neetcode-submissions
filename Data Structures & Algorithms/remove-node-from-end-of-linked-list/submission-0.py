# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        tot_len = 0
        while curr:
            tot_len =tot_len + 1
            curr = curr.next

        if tot_len < n:
            return head
        
        else:
            forward_len = tot_len - n

        if forward_len == 0:
            return head.next

        new_cur = head
        prev = head
        for i in range(forward_len):
            prev= new_cur
            new_cur = new_cur.next
        
        prev.next = new_cur.next

        return head