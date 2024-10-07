class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        for i in range(len(nums)-1,-1,-1):
            if count[nums[i]] == 1:
                return nums[i]
        return -1
            