# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []        
        if not root: 
            return res

        dq = deque()
        dq.append(root)
        dq_len = len(dq)
        while dq:
            dq_len = len(dq)
            sublist = []
            for _ in range(dq_len):
                node = dq.popleft()
                sublist.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(sublist)

        return res

        