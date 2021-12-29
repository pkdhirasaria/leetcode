# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append((root,root.val,[root.val]))
        ans = []
        while q:
            node,val,path = q.popleft()
            if node.left:
                q.append((node.left,node.left.val+val,path + [node.left.val]))
            if node.right:
                q.append((node.right,node.right.val+val,path +[node.right.val]))
            
            if (node.left,node.right) == (None,None) and val == targetSum:
                ans.append(path)
        return ans