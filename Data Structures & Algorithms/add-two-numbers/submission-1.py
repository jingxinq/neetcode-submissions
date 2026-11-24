# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 or curr2 or carry:
            sum_val = carry
            if curr1:
                sum_val += curr1.val
                curr1 = curr1.next
            if curr2:
                sum_val += curr2.val
                curr2 = curr2.next
            
            if sum_val >= 10:
                carry = 1
            else:
                carry = 0
            
            digit = sum_val % 10
            curr.next = ListNode(digit)
            curr = curr.next
 
        return dummy.next
            



            