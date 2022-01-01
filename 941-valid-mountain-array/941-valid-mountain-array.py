class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        n = len(a)
        if n < 3:
            return False
        inc = False
        dec = False
        for i in range(1,n):
            if a[i] > a[i-1]:
                inc = True
            else:
                break
        # print(i)
        if inc:
            # i -= 1
            while i < n:
                if a[i] < a[i-1]:
                    dec = True
                else:
                    break
                i+= 1
        # print(inc,dec,i)
        return inc and dec and i == n