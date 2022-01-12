class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 if a!=b else 0 for a,b in zip(heights,sorted(heights))])