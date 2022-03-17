class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import heapq
        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap,-n)
        a1 = heapq.heappop(heap)*-1
        a2 = heapq.heappop(heap)*-1
        return (a1-1)*(a2-1)