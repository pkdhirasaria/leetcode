class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        n = len(gs)
        for i in range(n):
            d[gs[i]].append(i)
        ans = []
        for g in d.keys():
            ng = []
            for m_id in d[g]:
                if len(ng) < g:
                    ng.append(m_id)
                else:
                    ans.append(ng)
                    ng = []
                    ng.append(m_id)
            if ng:
                ans.append(ng)
        return ans
                