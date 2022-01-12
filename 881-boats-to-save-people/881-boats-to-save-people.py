class Solution:
    def numRescueBoats(self, a: List[int], limit: int) -> int:
        a.sort()
        print(a)
        n = len(a)
        i = 0
        j = n-1
        boats = 0
        while i <= j:
            if a[j] == limit or a[i] + a[j] > limit:
                boats += 1
                j -=1
            else:
                boats += 1
                i +=1 
                j -=1
        return boats