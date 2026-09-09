# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        temp = head
        temp_prev = None
        if temp.next:
            temp_next = temp.next
        else:
            return head
        
        while temp.next:
            temp.next = temp_prev
            temp_prev = temp
            temp = temp_next
            temp_next = temp_next.next
        temp.next = temp_prev
        return temp