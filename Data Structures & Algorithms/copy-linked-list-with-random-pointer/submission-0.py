"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First pass: create a copy of each node, store in the map
        # Second pass: wire up next and random using the map lookups
        nodeMap = { None: None }
        
        cur1 = head
        while cur1:
            nodeMap[cur1] = Node(cur1.val)
            cur1 = cur1.next

        cur2 = head
        while cur2:
            copy = nodeMap[cur2]
            copy.next = nodeMap[cur2.next]
            copy.random = nodeMap[cur2.random]
            copy = copy.next
            cur2 = cur2.next
        return nodeMap[head]

