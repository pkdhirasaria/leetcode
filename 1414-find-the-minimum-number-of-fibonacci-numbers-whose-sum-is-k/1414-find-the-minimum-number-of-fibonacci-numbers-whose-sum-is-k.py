class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2: return 1
        ans = 0
        l = []
        a = 1
        b = 1
        l.append(a)
        l.append(b)
        while k > b:
            a,b = b,a+b
            l.append(b)
        # print(sum(l))
        i = len(l)-1
        while i > 0:
            if k >= l[i]:
                k -= l[i]
                ans += 1
            else:
                i -=1
        return ans