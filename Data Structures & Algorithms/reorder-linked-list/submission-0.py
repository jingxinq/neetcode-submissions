# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse 2nd LL
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        #merge the 2LL
        list1 = head
        list2 = prev
        while list2:
            temp_list1next = list1.next
            temp_list2next = list2.next
            list1.next = list2
            list2.next = temp_list1next
            list1 = temp_list1next
            list2 = temp_list2next

        return None
            
        