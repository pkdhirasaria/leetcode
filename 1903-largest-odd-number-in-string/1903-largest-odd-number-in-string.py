class Solution:
    def largestOddNumber(self, num: str) -> str:
        found = False
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 !=0:
                found = True
                break
        return num[:i+1] if found else ""