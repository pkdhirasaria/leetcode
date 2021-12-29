class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = x*-1
        r = int(''.join(list(reversed(str(x)))))
        if isNegative:
            r = r*-1
        # print(r)
        
        return r if pow(2,31)*-1 <= r < pow(2,31)-1 else 0