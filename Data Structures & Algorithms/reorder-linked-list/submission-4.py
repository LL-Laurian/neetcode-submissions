# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next:
            initial = head
            reverse_stack = []
            while head:
                reverse_stack.append(head.val)
                head = head.next
            
            
            curr = initial
            length = len(reverse_stack)
            isEven = length%2 ==0
            
            for i in range(length//2):
                temp = curr.next

                if (i == length//2-1 and isEven):
                    r = ListNode(reverse_stack.pop(), None)
                else:
                    r = ListNode(reverse_stack.pop(), temp)
                curr.next = r
                curr = temp
            
            curr.next = None    

