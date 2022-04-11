# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(root,Sum):
            if not root:
                return 0 
            right_sum = dfs(root.right,Sum)
            root.val += right_sum + Sum
            # Sum = root.valf
            left_sum = dfs(root.left,root.val)
            return root.val - Sum + left_sum
        dfs(root,0)
        return root
        