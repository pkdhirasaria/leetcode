class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for s,d in p:
            graph[s].append(d)
        vis = [-1]* n
        ans =[]
        # print(graph)
        def dfs(s):
            if vis[s] == 1:
                return True
            if vis[s] ==0:
                return False
            vis[s] = 0
            for g in graph[s]:
                if not  dfs(g):
                    return False
            ans.append(s)
            vis[s] =1
            return True
        
        for i in range(n):
            # print(vis)
            if not dfs(i):
                return []
        
        return ans