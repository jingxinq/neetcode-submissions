# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr_l1 = l1
        curr_l2 = l2
        carry = 0

        while curr_l1 or curr_l2 or carry:
            val1 = curr_l1.val if curr_l1 else 0 
            val2 = curr_l2.val if curr_l2 else 0 
            sum_val = val1 + val2 + carry
            print(sum_val)

            if sum_val >= 10:
                carry = 1
            else:
                carry = 0
            
            res_val = sum_val % 10
            print(res_val)
            curr.next = ListNode(res_val)

            if curr_l1:
                curr_l1 = curr_l1.next 
            if curr_l2:
                curr_l2 = curr_l2.next 
            curr = curr.next

        return dummy.next


        