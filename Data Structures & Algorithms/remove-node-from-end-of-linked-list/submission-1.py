# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        if n == length:
            return head.next
        k = length - n - 1
        curr = head
        while k > 0:
            k -= 1
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return head
        
        

