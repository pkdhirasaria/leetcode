class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans  = sum_so_far = nums[0]
        for n in nums[1:]:
            sum_so_far = max(n,sum_so_far+ n)
            ans = max(ans,sum_so_far)
        return ans