# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        prev_l = None
        l = head
        if left > 1:
            for i in range(1 , left):
                prev_l = l
                l = l.next
        r = l
        for _ in range(1 , right - left + 1):
            r = r.next
        store_r = r.next
        store_l = l
        curr = None
        temp = l

        for _ in range(right - left + 1):
            store = temp.next
            temp.next = curr
            curr = temp
            temp = store
        store_l.next = store_r
        if prev_l:
            prev_l.next = curr 
            return head
        return curr
        
        