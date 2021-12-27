class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        def bisect_left(a, x,index):
            i = 0
            j = index
            while i < j:
                mid = (i + j)//2
                if a[mid] > x:
                    j = mid
                else:
                    i = mid+1
            return j
        ages.sort()
        count= 0
        d = defaultdict(int)
        for i in range(len(ages)-1,-1,-1):
            if ages[i] not in d:
                left = bisect_left(ages,0.5*ages[i] + 7,i)
                d[ages[i]] = i - left
                count += (i-left)
                # print(ages[i],i,left,count)
            else:
                count += d[ages[i]]
        # print(count)    
        # print(sorted(ages))
        # print(sorted([0.5*x + 7 for x in ages]))
        
        return count