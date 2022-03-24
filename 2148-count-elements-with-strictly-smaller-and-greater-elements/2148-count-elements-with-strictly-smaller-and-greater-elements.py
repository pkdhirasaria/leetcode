class Solution:
    def countElements(self, nums: List[int]) -> int:
        c=0
        from collections import Counter
        d=Counter(nums)
        nums=list(set(nums))
        nums.sort()
        for i in range(1,len(nums)-1):
            if nums[i]<nums[i+1] and nums[i]>nums[i-1]:
                c+=d[nums[i]]
        return c