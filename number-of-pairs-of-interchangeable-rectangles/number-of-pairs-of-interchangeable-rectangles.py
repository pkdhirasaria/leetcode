class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios =[]
        for h,w in rectangles:
            ratios.append(h/w)
        ans = 0
        d = defaultdict(int)
        for r in ratios:
            if r in d:
                ans += d[r]
            d[r] += 1
        return ans