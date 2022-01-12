class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_so_far = nums[0]
        res =nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                max_so_far += nums[i]
            else:
                res = max(res,max_so_far)
                max_so_far = nums[i]
        res = max(res,max_so_far)
        return res