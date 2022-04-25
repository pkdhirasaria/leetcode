class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        class DSU:
            
            def __init__(self,n):
                self.parent = [i for i in range(n)]
                self.rank = [0]*n
            
            def find(self,x):
                if x != self.parent[x] : self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                x = self.find(x)
                y = self.find(y)
                
                if self.rank[x] > self.rank[y]:
                    self.parent[x] = y
                    self.rank[x] += self.rank[y]
                else:
                    self.parent[y] = x
                    self.rank[y] += self.rank[x]
        n = len(isConnected)
        uf = DSU(n)
        parents =set()
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i,j)
                    x = uf.find(i)
                    y = uf.find(j)
                    parents.add(x)
                    parents.add(y)
        # print(uf.parent,uf.rank)
        # print(parents)
        return len(set([uf.find(i) for i in range(n)]))
                    
                