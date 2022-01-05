# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.res = 0
        def dfs(root,targetSum,prev_sum):
            if not root:
                return
            prev_sum += root.val
            self.res += prefix[prev_sum-targetSum]
            prefix[prev_sum] += 1
            
            dfs(root.left,targetSum,prev_sum)
            dfs(root.right,targetSum,prev_sum)
            
            prefix[prev_sum] -= 1
        dfs(root,targetSum,0)    
                
        return self.res