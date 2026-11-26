# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #need to pass in max_val hence need another functio

        def dfs(node, max_val) -> int:
            count = 0
            # base case
            if not node:
                return 0
            
            # condition
            if node.val >= max_val:
                count = 1
                max_val = max(node.val, max_val)

            #recursion
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

            #return value
            return left + right + count

        return dfs(root, root.val)
        