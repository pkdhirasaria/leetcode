class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        import heapq
        from collections import Counter
        i = 0
        heap = []
        heapq.heapify(heap)
        for m in mat:
            heapq.heappush(heap,(Counter(m)[1],i))
            i +=1
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -=1
        return res