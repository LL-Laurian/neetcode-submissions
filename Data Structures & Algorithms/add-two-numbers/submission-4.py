# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        res = head
        remain = 0

        while l1 and l2:
            total = l1.val + l2.val + remain
            print("Total", total)
            if total >= 10:
                res.next = ListNode(total - 10)
                remain = 1
            
            else:
                res.next = ListNode(total)
                remain = 0

            l1 = l1.next
            l2 = l2.next
            res = res.next


        while l1:
            total = l1.val + remain
            if total >= 10:
                res.next = ListNode(total - 10)
                remain = 1
            
            else:
                res.next = ListNode(total)
                remain = 0

            l1 = l1.next
            res = res.next
            
        
        while l2:
            total = l2.val + remain
            if total >= 10:
                res.next = ListNode(total - 10)
                remain = 1
            
            else:
                res.next = ListNode(total)
                remain = 0

            l2 = l2.next
            res = res.next

        if remain == 1:
            res.next = ListNode(1)

        return head.next