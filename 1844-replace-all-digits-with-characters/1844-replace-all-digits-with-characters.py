class Solution:
    def replaceDigits(self, s: str) -> str:
        return ''.join([s[i] if i %2 == 0 else chr(ord(s[i-1] ) - 96 + int(s[i]) + 96) for i in range(len(s)) ])