# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root,lookup):
            if not root:
                return []
            lookup[root] = [root.val]
            for val in dfs(root.left,lookup):
                lookup[root].append(root.val + val)
            for val in dfs(root.right,lookup):
                lookup[root].append(root.val + val)    
            return lookup[root]
        lookup = {}
        count =0
        dfs(root,lookup)
        for l in lookup:
            for val in lookup[l]:
                if val == targetSum:
                    count += 1
        return count
                
#         prefix = defaultdict(int)
#         prefix[0] = 1
#         self.res = 0
#         def dfs(root,targetSum,prev_sum):
#             if not root:
#                 return
#             prev_sum += root.val
#             self.res += prefix[prev_sum-targetSum]
#             prefix[prev_sum] += 1
            
#             dfs(root.left,targetSum,prev_sum)
#             dfs(root.right,targetSum,prev_sum)
            
#             prefix[prev_sum] -= 1
#         dfs(root,targetSum,0)    
                
        # return self.res