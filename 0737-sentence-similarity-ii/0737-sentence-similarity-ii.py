class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        graph = defaultdict(list)
        for a,b in similarPairs:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(src,dest,parent):
            q = deque()
            q.append((src,parent))
            v = set()
            v.add(src)
            while q:
                node,p = q.popleft()
                for g in graph[node]:
                    if g not in v and g != p:
                        if g == dest:
                            return True
                        v.add(g)
                        q.append((g,p))
            return False

        # print(graph)
        for s1,s2 in zip(sentence1,sentence2):
            if s1 != s2 and not bfs(s1,s2,s1):
                return False
        return True
