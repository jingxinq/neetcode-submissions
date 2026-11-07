# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split into 2
        second = slow.next
        slow.next = None

        # reverse the second
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l2 = prev

        # join the 2, head and l2
        curr1, curr2 = head, l2
        while curr1 and curr2:
            nxt1, nxt2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = nxt1
            curr1, curr2 = nxt1, nxt2


