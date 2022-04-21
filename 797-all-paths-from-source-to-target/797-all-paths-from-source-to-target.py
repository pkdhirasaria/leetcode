class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        self.ans = []
        def dfs(node,path):
            if node == n-1:
                # print(path)
                self.ans.append(path.copy())
                # print(self.ans)
                return
            for g in graph[node]:
                path.append(g)
                # print(node,g,path)
                dfs(g,path)
                path.pop()
                # print(node,g,path)
            return
        path = []
        path.append(0)
        dfs(0,path)
        return self.ans