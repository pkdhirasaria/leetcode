class Solution:
    def goodDaysToRobBank(self, a: List[int], time: int) -> List[int]:
        n = len(a)
        left = [0]*n
        right = [0]*n
        
        for i in range(1,n):
            if a[i-1] >= a[i]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 0
        for i in range(n-2,-1,-1):
            if a[i] <= a[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 0
        # print(left,right)
        # return []
        ans = []
        for i in range(n):
            if left[i] >=time and right[i] >=time:
                ans.append(i)
        return ans
        
            