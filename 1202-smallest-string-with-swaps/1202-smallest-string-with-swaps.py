class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n): 
                self.p = list(range(n))
                self.rank = [0]*n
            def union(self, x, y): 
                x = self.find(x)
                y = self.find(y)
                if x == y:
                    return 
                if self.rank[x] > self.rank[y]:
                    self.p[y] = x
                else:
                    self.p[x] = y
                    self.rank[y] += 1
                # self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if x != self.p[x]: self.p[x] = self.find(self.p[x])
                return self.p[x]
        uf, res, m = UF(len(s)), [], defaultdict(list)
        for x,y in pairs: 
            uf.union(x,y)
        for i in range(len(s)): 
            m[uf.find(i)].append(s[i])
        # print(m)
        for comp_id in m.keys(): 
            m[comp_id].sort(reverse=True)
        # print(m)
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())
        return ''.join(res)