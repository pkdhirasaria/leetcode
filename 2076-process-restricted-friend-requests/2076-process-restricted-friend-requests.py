class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        class DSU:

            def __init__(self,n):
                self.parent = list(range(n))
                self.rank = [0] *n
            
            def find(self,x):
                if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                x,y = self.find(x), self.find(y)
                if x==y:
                    return False
                if self.rank[x] > self.rank[y]:
                    self.parent[y] = x
                else:
                    self.parent[x] = y
                    self.rank[y] += 1
                return True
        uf = DSU(n)
        ans = []
        # print(d)
        for a,b in requests:
            x,y = uf.find(a),uf.find(b)
            res = True
            for c,d in restrictions:
                pc,pd = uf.find(c),uf.find(d)
                if set([pc,pd]) == set([x,y]):
                    res = False
                    break
            if res:
                uf.parent[x] = y
                # uf.union(x,y)
            ans.append(res)
            
                # a
            
        # print(uf.parent,uf.rank,ans)
        return ans