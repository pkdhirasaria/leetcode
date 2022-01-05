# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.depth = 0
        self.lca = None
        # print(root.val,d)
        def dfs(root,d):
            
            self.depth = max(self.depth,d)
            if not root:
                return d
            
            left = dfs(root.left,d+1) 
            right = dfs(root.right,d+1) 
            if left == right == self.depth:
                self.lca = root
                self.depth = left
            # print(root.val,d,self.depth,self.lca if not self.lca else self.lca.val)
            return max(left,right) 
        dfs(root,0)
        return self.lca