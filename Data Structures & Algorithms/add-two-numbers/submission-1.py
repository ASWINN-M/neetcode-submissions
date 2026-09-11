# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 , num2 = "" , ""

        temp1 , temp2 = l1 , l2
        while temp1:
            num1 += str(temp1.val)
            temp1 = temp1.next
        
        while temp2:
            num2 += str(temp2.val)
            temp2 = temp2.next
        
        res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        dummynode = ListNode(None)
        curr = dummynode
        head = dummynode
        for i in res:
            curr.val = int(i)
            newnode = ListNode(None)
            curr.next = newnode

            prev = curr
            curr = newnode
        prev.next = None
        return head
