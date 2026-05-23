# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        curr = None
        while temp:
            store = temp.next
            temp.next = curr
            curr = temp
            temp = store
            
        return curr
