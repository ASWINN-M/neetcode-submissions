# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        temp = head

    
        while temp.next:
            length += 1
            temp = temp.next
        del_node = length - n 

        if del_node == 0:
            return head.next
        ptr = 0
        temp = head
        while temp and ptr != del_node - 1:
            temp = temp.next
            ptr += 1
        temp.next = temp.next.next
        return head
