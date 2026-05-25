# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rev(linked_list):
            curr = None
            temp = linked_list

            while temp:
                store = temp.next
                temp.next = curr
                curr = temp
                temp = store
            return curr
        
        temp = head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        dummy = ListNode(0)
        curr = dummy
        itr = length // k
        for i in range(itr):
            temp = head
            for i in range(k - 1):
                temp = temp.next
            store = temp.next
            temp.next = None
            curr.next = rev(head)
            while curr.next:
                curr = curr.next
            head = store
        curr.next = head
        return dummy.next
        
        
