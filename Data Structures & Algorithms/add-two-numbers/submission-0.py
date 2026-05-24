# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 , temp2 = l1 , l2
        a = ""
        while temp1:
            a += str(temp1.val)
            temp1 = temp1.next
        a = a[::-1]
        b = ""

        while temp2:
            b += str(temp2.val)
            temp2 = temp2.next
        b = b[::-1]
        c = str(int(a) + int(b))
        head = ListNode(None)
        curr = head 
        for i in c[::-1]:
            newNode = ListNode(int(i))
            curr.next = newNode
            curr = curr.next
        return head.next
            