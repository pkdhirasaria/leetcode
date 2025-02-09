class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        ans = 0
        while j < n:
            if nums[j] == 1:
                j += 1
            else:
                if k > 0:
                    j += 1
                    k -= 1
                else:
                    ans = max(ans, j-i)
                    while  i < n and nums[i] == 1:
                        i += 1
                    i += 1
                    ans = max(ans, j-i)
                    j += 1
            ans = max(ans, j-i)
        return ans
