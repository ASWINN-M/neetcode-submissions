# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head , head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        prev = None
        while temp:
            store = temp.next
            temp.next = prev
            prev = temp
            temp = store
        
        curr = head
        temp = prev
        while temp and curr:
            store_curr = curr.next
            store_temp = temp.next
            curr.next = temp
            temp.next = store_curr

            curr = store_curr
            temp = store_temp
            

