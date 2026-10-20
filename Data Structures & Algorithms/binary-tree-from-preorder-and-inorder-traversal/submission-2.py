# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - root, left ,right
        # inorder - left, root, right

        indices = {}
        for i, val in enumerate(inorder):
            indices[val] = i

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None
            #find root in preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            #find index of root in inorder
            mid = indices[root_val]
            #build the left and right
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
         
        return dfs(0, len(preorder)-1)

