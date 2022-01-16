"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(root,h):
            if not root or not root.children:
                return h
            t =0
            for c in root.children:
                t = max(t,dfs(c,h+1))
            return t
        return dfs(root,1)