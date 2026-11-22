# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        len_ll = 0
        while fast:
            len_ll += 1
            fast = fast.next

        n_front = len_ll - n
        
        if n_front == 0:
            return head.next

        for _ in range(n_front-1):
            slow = slow.next
        
        slow.next = slow.next.next
        return head