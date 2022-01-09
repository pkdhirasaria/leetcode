class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], edges: List[List[int]]) -> int:
        class DSU:
            
            def __init__(self,n=10**6):
                self.parent = list(range(n))
                self.rank = [0]*n
            
            def find(self,x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                x,y = self.find(x),self.find(y)
                if x == y:
                    return
                if self.rank[x] > self.rank[y]:
                    self.parent[y] = x
                else:
                    self.parent[x] = y
                    self.rank[y] += 1
        uf = DSU(len(source))
        for a,b in edges:
            uf.union(a,b)
        d = defaultdict(set)
        for i in range(len(source)):
            d[uf.find(i)].add(i)
        ans =0                
        # print(d)
        for indices in d.values():
            A = [source[i] for i in indices]
            B = [target[i] for i in indices]
            # print(Counter(A)-Counter(B))
            ans += sum((Counter(A)-Counter(B)).values())
        return ans
                