# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        d = defaultdict(list)
        def dfs(node, par = None):
            if node:
                d[node].append(par)
                d[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        queue = deque(node for node in d if node and node.val == k)
        seen = set(queue)
        while queue:
            node = queue.popleft()
            if node:
                if len(d[node]) <=1:
                    return node.val
                for g in d[node]:
                    if g not in seen:
                        seen.add(g)
                        queue.append(g)