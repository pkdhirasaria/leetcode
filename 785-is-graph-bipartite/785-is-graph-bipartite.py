class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque,defaultdict
        q = deque()
        g = defaultdict(list)
        # for node,edges in enumerate(graph):
        #     g[node].append()
        q.append((0,1))
        color = {}
        color[0] = 1
        vis = set()
        vis.add(0)
        for i in range(1,len(graph)):
            if i not in vis:
                if not q:
                    q.append((i,1))
                while  q:
                    edge, c = q.popleft()
                    for node in graph[edge]:
                        if node not in vis:
                            color[node] = c*-1
                            q.append((node, c * -1))
                            vis.add(node)
                        else:
                            if color[node] == c:
                                return False
        return True