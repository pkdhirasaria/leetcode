# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append((root,chr(root.val+97)))
        ans = '~'
        while q:
            node,val = q.popleft()
            # print(node.val,val)
            if (node.left,node.right) == (None,None): 
                ans = min(ans,val)
            if node.left:
                q.append((node.left,chr(node.left.val + 97) + val))
            if node.right:
                q.append((node.right,chr(node.right.val + 97) + val))
        return ans
        
        # def dfs(root):
        #     if (root.left,root.right) == (None,None):
        #         return chr(root.val + 97)
        #     left,right = '',''
        #     if root.left:
        #         left = dfs(root.left)
        #     if root.right:
        #         right = dfs(root.right)
        #     r = chr(root.val + 97)
        #     print(left,right,left+r,right+r)
        #     if left+r < right + r:
        #         return left + r
        #     else:
        #         return right + r
        # return dfs(root)