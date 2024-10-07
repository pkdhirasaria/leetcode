class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = -1
        for k,v in c.items():
            if v == 1:
                m = max(m,k)
        return m
        